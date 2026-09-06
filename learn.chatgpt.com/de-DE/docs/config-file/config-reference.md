<!-- source: https://learn.chatgpt.com/de-DE/docs/config-file/config-reference -->

Nutze diese Seite als durchsuchbare Referenz für Codex-Konfigurationsdateien. Erläuterungen zu den Konzepten und Beispiele findest du unter [Grundlagen der Konfiguration](/de-DE/codex/config-file/config-basic) und [Erweiterte Konfiguration](/de-DE/codex/config-file/config-advanced).

## `config.toml`

Die Konfiguration auf Benutzerebene befindet sich in `~/.codex/config.toml`. Du kannst außerdem projektspezifische Überschreibungen in Dateien namens `.codex/config.toml` hinzufügen. Codex lädt projektspezifische Konfigurationsdateien nur, wenn du dem Projekt vertraust.

Projektspezifische Konfigurationen können folgende auf dem Rechner festgelegte Werte nicht überschreiben: Anbieter- und Authentifizierungseinstellungen,
vom Host verwaltete Metadaten für App-Anfragen, Benachrichtigungseinstellungen und die Auswahl des Konfigurationsprofils
sowie Schlüssel für das Telemetrie-Routing. Codex ignoriert `openai_base_url`,
`chatgpt_base_url`, `apps_mcp_product_sku`, `model_provider`,
`model_providers`, `notify`, `profile`, `profiles`,
`experimental_realtime_ws_base_url` und `otel`, wenn sie in einer
projektspezifischen Konfigurationsdatei namens `.codex/config.toml` vorkommen. Lege stattdessen die Schlüssel für Anbieter, Benachrichtigungen und Telemetrie
in der Konfiguration auf Benutzerebene ab. Die [Profildateien](/de-DE/codex/config-file/config-advanced#profiles) für die Konfiguration liegen im selben Verzeichnis wie
`config.toml` und haben den Pfad `$CODEX_HOME/profile-name.config.toml`. Wähle eine davon mit
`--profile profile-name` aus.

Nutze diese Referenz für Konfigurationsschlüssel zu Sandbox und Genehmigungen (`approval_policy`, `sandbox_mode` und `sandbox_workspace_write.*`) zusammen mit [Sandbox und Genehmigungen](/de-DE/codex/agent-approvals-security#sandbox-and-approvals), [Geschützte Pfade in Stammverzeichnissen mit Schreibzugriff](/de-DE/codex/agent-approvals-security#protected-paths-in-writable-roots) und [Netzwerkzugriff](/de-DE/codex/agent-approvals-security#network-access). Informationen zu Berechtigungsprofilen in der Betaphase findest du unter [Berechtigungen](/de-DE/codex/permissions).

<ConfigTable
  options={[
    {
      key: "model",
      type: "string",
      description: "Zu verwendendes Modell (z. B. `gpt-5.5`).",
    },
    {
      key: "review_model",
      type: "string",
      description:
        "Optionales abweichendes Modell für `/review` (standardmäßig wird das Modell der aktuellen Sitzung verwendet).",
    },
    {
      key: "model_provider",
      type: "string",
      description: "Anbieter-ID aus `model_providers` (Standard: `openai`).",
    },
    {
      key: "openai_base_url",
      type: "string",
      description:
        "Abweichende Basis-URL für den integrierten Modellanbieter `openai`.",
    },
    {
      key: "model_context_window",
      type: "number",
      description: "Anzahl der für das aktive Modell verfügbaren Token im Kontextfenster.",
    },
    {
      key: "model_auto_compact_token_limit",
      type: "number",
      description:
        "Token-Schwellenwert, der die automatische Compaction (Kontextverdichtung) des Verlaufs auslöst (wenn nicht festgelegt, gelten die Standardwerte des Modells).",
    },
    {
      key: "model_auto_compact_token_limit_scope",
      type: "total | body_after_prefix",
      description:
        "Steuert, ob für den Schwellenwert der automatischen Compaction (Kontextverdichtung) der gesamte aktive Kontext (`total`, der Standardwert) oder nur der Zuwachs nach dem übernommenen Präfix des Compaction-Fensters (`body_after_prefix`) berücksichtigt wird.",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description:
        "Optionaler Pfad zu einem JSON-Modellkatalog, der beim Start geladen wird. Eine ausgewählte Profildatei `$CODEX_HOME/profile-name.config.toml` kann diesen Wert für das jeweilige Profil überschreiben.",
    },
    {
      key: "oss_provider",
      type: "lmstudio | ollama",
      description:
        "Standardmäßig verwendeter lokaler Anbieter bei der Ausführung mit `--oss` (wenn nicht festgelegt, fragt Codex danach).",
    },
    {
      key: "approval_policy",
      type: "untrusted | on-request | never | { granular = { sandbox_approval = bool, rules = bool, mcp_elicitations = bool, request_permissions = bool, skill_approval = bool } }",
      description:
        "Steuert, wann Codex vor dem Ausführen von Befehlen auf eine Genehmigung wartet. Du kannst außerdem `approval_policy = { granular = { ... } }` verwenden, um bestimmte Kategorien von Anfragen zuzulassen oder automatisch abzulehnen, während andere Anfragen interaktiv bleiben. `on-failure` ist veraltet; verwende `on-request` für interaktive Ausführungen oder `never` für nicht interaktive Ausführungen.",
    },
    {
      key: "approval_policy.granular.sandbox_approval",
      type: "boolean",
      description:
        "Bei `true` dürfen Genehmigungsanfragen für eine Sandbox-Eskalation angezeigt werden.",
    },
    {
      key: "approval_policy.granular.rules",
      type: "boolean",
      description:
        "Bei `true` dürfen Genehmigungsanfragen angezeigt werden, die durch `prompt`-Regeln von execpolicy ausgelöst werden.",
    },
    {
      key: "approval_policy.granular.mcp_elicitations",
      type: "boolean",
      description:
        "Bei `true` dürfen Anfragen zur MCP-Elizitation angezeigt werden, statt automatisch abgelehnt zu werden.",
    },
    {
      key: "approval_policy.granular.request_permissions",
      type: "boolean",
      description:
        "Bei `true` dürfen Anfragen des Tools `request_permissions` angezeigt werden.",
    },
    {
      key: "approval_policy.granular.skill_approval",
      type: "boolean",
      description:
        "Bei `true` dürfen Genehmigungsanfragen für Skill-Skripte angezeigt werden.",
    },
    {
      key: "approvals_reviewer",
      type: "user | auto_review",
      description:
        "Legt fest, wer die bei `on-request` oder granularen Genehmigungsrichtlinien infrage kommenden Genehmigungsanfragen prüft. Standardmäßig ist dies `user`; bei `auto_review` übernimmt der für die Überprüfung zuständige Subagent die Prüfung. Diese Einstellung ändert nichts am Sandboxing und führt nicht dazu, dass innerhalb der Sandbox bereits erlaubte Aktionen überprüft werden.",
    },
    {
      key: "auto_review.policy",
      type: "string",
      description:
        "Lokale Richtlinienanweisungen in Markdown für die automatische Überprüfung. Die verwaltete Einstellung `guardian_policy_config` hat Vorrang. Leere Werte werden ignoriert.",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description:
        "Erlaubt Tools auf Shell-Basis, die Semantik einer Login-Shell zu verwenden. Standardmäßig `true`; bei `false` werden Anfragen mit `login = true` abgelehnt, und bei nicht angegebenem `login` werden standardmäßig Shells ohne Login verwendet.",
    },
    {
      key: "sandbox_mode",
      type: "read-only | workspace-write | danger-full-access",
      description:
        "Sandbox-Richtlinie für Dateisystem- und Netzwerkzugriff während der Befehlsausführung.",
    },
    {
      key: "sandbox_workspace_write.writable_roots",
      type: "array<string>",
      description:
        "Zusätzliche Stammverzeichnisse mit Schreibzugriff bei `sandbox_mode = \"workspace-write\"`.",
    },
    {
      key: "sandbox_workspace_write.network_access",
      type: "boolean",
      description:
        "Ausgehenden Netzwerkzugriff innerhalb der workspace-write-Sandbox zulassen.",
    },
    {
      key: "sandbox_workspace_write.exclude_tmpdir_env_var",
      type: "boolean",
      description:
        "`$TMPDIR` im workspace-write-Modus aus den Stammverzeichnissen mit Schreibzugriff ausschließen.",
    },
    {
      key: "sandbox_workspace_write.exclude_slash_tmp",
      type: "boolean",
      description:
        "`/tmp` im workspace-write-Modus aus den Stammverzeichnissen mit Schreibzugriff ausschließen.",
    },
    {
      key: "windows.sandbox",
      type: "unelevated | elevated",
      description:
        "Nativer Sandbox-Modus nur für Windows, wenn Codex nativ unter Windows ausgeführt wird.",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "Wenn Codex nativ unter Windows läuft, wird der abschließende Unterprozess in der Sandbox standardmäßig auf einem privaten Desktop ausgeführt. Setze den Wert nur auf `false`, wenn du Kompatibilität mit dem älteren Verhalten von `Winsta0\\\\Default` benötigst.",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "Setze den Wert auf `false`, um den Zugriff auf den Browserverlauf einzuschränken. Verwaltete Vorgaben können diese Einschränkung erzwingen.",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "Standardbeschränkungen für Browser-Origins. Unterstützt `access`, `uploads`, `downloads` und `full_cdp_access`, jeweils mit dem Wert `allow` oder `deny`.",
    },
    {
      key: "browser_use.origins.<origin>",
      type: "table",
      description:
        "Browsereinschränkungen pro Origin mit denselben Feldern wie `browser_use.default_origin_policy`. Gib ein HTTP- oder HTTPS-Schema und optional einen Port an; lasse Pfade, Abfrageparameter und Fragmente weg. Lokale Werte können verwaltete Verbote nicht lockern.",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "Standardrichtlinie für den Zugriff auf native Apps bei der Computernutzung. App-spezifische Einträge können eine Richtlinie vorgeben; die lokale Konfiguration kann verwaltete Einschränkungen nicht lockern.",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description: "Zugriff auf native macOS-Apps mit der Bundle-Kennung als Schlüssel.",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "Zugriff auf paketierte Windows-Apps mit der Application User Model ID (AUMID) als Schlüssel.",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "Zugriffsregeln für ausführbare Windows-Dateien. Jede Regel erfordert `publisher_name`, `product_name` und `access` (`allow` oder `deny`); `binary_name` ist optional.",
    },
    {
      key: "computer_use.windows.always_allowed_app_ids",
      type: "array<string>",
      description:
        "Kennungen von Windows-Apps, die über die Computernutzung ohne Rückfrage geöffnet werden können. Apps, die nicht in der Liste stehen, erfordern eine Genehmigung. Entferne gespeicherte Einträge aus den Einstellungen für die Computernutzung der ChatGPT-Desktop-App.",
    },
    {
      key: "notify",
      type: "array<string>",
      description:
        "Befehl, der für Benachrichtigungen aufgerufen wird; erhält eine JSON-Nutzlast von Codex.",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description:
        "Beim Start nach Codex-Updates suchen (nur auf false setzen, wenn Updates zentral verwaltet werden).",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "Übermittlung von Feedback über `/feedback` in allen lokalen Clients aktivieren (Standard: true).",
    },
    {
      key: "analytics.enabled",
      type: "boolean",
      description:
        "Analysen für diesen Rechner oder dieses Profil aktivieren oder deaktivieren. Wenn nicht festgelegt, gilt der Standardwert des Clients.",
    },
    {
      key: "instructions",
      type: "string",
      description:
        "Für die zukünftige Verwendung reserviert; verwende vorzugsweise `model_instructions_file` oder `AGENTS.md`.",
    },
    {
      key: "developer_instructions",
      type: "string",
      description:
        "Zusätzliche Entwickleranweisungen, die in die Sitzung eingebunden werden (optional).",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description:
        "Verzeichnis, in das Codex Protokolldateien schreibt; Standard ist `$CODEX_HOME/log`. Wenn du es explizit festlegst, wird in diesem Verzeichnis auch das optionale TUI-Klartextprotokoll `codex-tui.log` aktiviert.",
    },
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "Verzeichnis, in dem Codex die SQLite-basierte Zustandsdatenbank für Agentenaufträge und andere fortsetzbare Laufzeitzustände speichert.",
    },
    {
      key: "compact_prompt",
      type: "string",
      description: "Inline-Überschreibung für den Prompt zur Compaction (Kontextverdichtung) des Verlaufs.",
    },
    {
      key: "model_instructions_file",
      type: "string (path)",
      description:
        "Ersatz für die integrierten Anweisungen; wird anstelle von `AGENTS.md` verwendet.",
    },
    {
      key: "personality",
      type: "none | friendly | pragmatic",
      description:
        "Standardmäßiger Kommunikationsstil für Modelle, die `supportsPersonality` signalisieren. Kann für einzelne Threads oder Turns oder über `/personality` überschrieben werden.",
    },
    {
      key: "service_tier",
      type: "string",
      description:
        "Bevorzugte Servicestufe für neue Turns. Verwende `fast` oder eine andere vom aktiven Modell angebotene Stufe; `fast` wird dem Anfragewert `priority` zugeordnet.",
    },
    {
      key: "experimental_compact_prompt_file",
      type: "string (path)",
      description:
        "Überschreibung für den Prompt zur Compaction (Kontextverdichtung) aus einer Datei laden (experimentell).",
    },
    {
      key: "skills.max_context_tokens",
      type: "integer (positive)",
      description:
        "Token-Budget für den Katalog der verfügbaren Skills. Standardmäßig 2 % des Kontextfensters des Modells. Explizit angegebene Werte sind auf `10000` Token begrenzt.",
    },
    {
      key: "skills.config",
      type: "array<object>",
      description: "In config.toml gespeicherte Vorgaben, die den Aktivierungsstatus einzelner Skills überschreiben.",
    },
    {
      key: "skills.config.<index>.path",
      type: "string (path)",
      description: "Pfad zu einem Skill-Ordner, der `SKILL.md` enthält.",
    },
    {
      key: "skills.config.<index>.enabled",
      type: "boolean",
      description: "Den angegebenen Skill aktivieren oder deaktivieren.",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "Eine bestimmte App oder einen bestimmten Konnektor anhand der ID aktivieren oder deaktivieren (Standard: true).",
    },
    {
      key: "apps._default.enabled",
      type: "boolean",
      description:
        "Legt fest, ob Apps standardmäßig aktiviert sind, sofern dies nicht für eine einzelne App überschrieben wird.",
    },
    {
      key: "apps._default.destructive_enabled",
      type: "boolean",
      description:
        "Legt fest, ob App-Tools mit `destructive_hint = true` standardmäßig zugelassen oder abgelehnt werden.",
    },
    {
      key: "apps._default.open_world_enabled",
      type: "boolean",
      description:
        "Legt fest, ob App-Tools mit `open_world_hint = true` standardmäßig zugelassen oder abgelehnt werden.",
    },
    {
      key: "apps._default.approvals_reviewer",
      type: "user | auto_review",
      description:
        "Legt fest, wer Genehmigungsanfragen für App-Tools standardmäßig prüft, sofern dies nicht für eine einzelne App überschrieben wird. Ohne Angabe übernehmen Apps den Wert `approvals_reviewer` der obersten Ebene.",
    },
    {
      key: "apps._default.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Standardverhalten bei Genehmigungen für App-Tools, sofern keine Überschreibung auf App- oder Tool-Ebene vorliegt.",
    },
    {
      key: "apps.<id>.destructive_enabled",
      type: "boolean",
      description:
        "Tools in dieser App, die `destructive_hint = true` angeben, zulassen oder blockieren.",
    },
    {
      key: "apps.<id>.open_world_enabled",
      type: "boolean",
      description:
        "Tools in dieser App, die `open_world_hint = true` angeben, zulassen oder blockieren.",
    },
    {
      key: "apps.<id>.default_tools_enabled",
      type: "boolean",
      description:
        "Legt fest, ob Tools in dieser App standardmäßig aktiviert sind, sofern für das jeweilige Tool keine abweichende Einstellung vorliegt.",
    },
    {
      key: "apps.<id>.approvals_reviewer",
      type: "user | auto_review",
      description:
        "Prüfinstanz für Genehmigungsanfragen der Tools dieser App. Überschreibt `apps._default.approvals_reviewer`.",
    },
    {
      key: "apps.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Standardmäßiges Genehmigungsverhalten für Tools in dieser App, sofern für das jeweilige Tool keine abweichende Einstellung vorliegt.",
    },
    {
      key: "apps.<id>.tools.<tool>.enabled",
      type: "boolean",
      description:
        "Abweichende Aktivierungseinstellung für ein einzelnes App-Tool (zum Beispiel `repos/list`).",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "Abweichendes Genehmigungsverhalten für ein einzelnes App-Tool.",
    },
    {
      key: "tool_suggest.discoverables",
      type: "array<table>",
      description:
        "Tool-Vorschläge für weitere auffindbare Konnektoren oder Plug-ins zulassen. Jeder Eintrag verwendet `type = \"connector\"` oder `\"plugin\"` und eine `id`.",
    },
    {
      key: "tool_suggest.disabled_tools",
      type: "array<table>",
      description:
        "Vorschläge für bestimmte auffindbare Konnektoren oder Plug-ins deaktivieren. Jeder Eintrag verwendet `type = \"connector\"` oder `\"plugin\"` und eine `id`.",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "App-Integrationen (Konnektoren) aktivieren (stabil; standardmäßig aktiviert). Der Datenverkehr von Apps und Konnektoren wird nicht durch den Netzwerkproxy für Befehle in der Sandbox oder dessen Domain-Zulassungsliste kontrolliert.",
    },
    {
      key: "features.hooks",
      type: "boolean",
      description:
        "Lifecycle-Hooks aktivieren, die aus `hooks.json` oder aus der Inline-Konfiguration `[hooks]` geladen werden. `features.codex_hooks` ist ein veralteter Alias.",
    },
    {
      key: "features.code_mode.enabled",
      type: "boolean",
      description:
        "Konfiguration für die Code-Modus-Funktion aktivieren. Diese Funktion befindet sich in der Entwicklung und ist standardmäßig deaktiviert.",
    },
    {
      key: "features.code_mode.excluded_tool_namespaces",
      type: "array<string>",
      description:
        "Tool-Namespaces, die der Code-Modus weder in Anleitungen für verschachtelte Code-Modus-Tools einbezieht noch dem Executor bereitstellt.",
    },
    {
      key: "features.code_mode.direct_only_tool_namespaces",
      type: "array<string>",
      description:
        "Tool-Namespaces, die der Code-Modus nur über direkte Tool-Aufrufe verwenden kann.",
    },
    {
      key: "features.context_management.experimental_mode",
      type: "boolean",
      description:
        "Experimentelle Kontextverwaltung aktivieren (standardmäßig deaktiviert). Sie verwendet Notizen und einen durchsuchbaren Verlauf, um gesammelte Details zu bewahren, statt den Kontext wiederholt zu einer einzigen Zusammenfassung zu verdichten. Erfordert eine ChatGPT-Anmeldung mit Plus, Pro oder Pro Lite.",
    },
    {
      key: "features.rollout_budget.enabled",
      type: "boolean",
      description:
        "Nachverfolgung des Rollout-Budgets aktivieren. Diese Funktion befindet sich in der Entwicklung und ist standardmäßig deaktiviert. Bei Aktivierung ist `features.rollout_budget.limit_tokens` erforderlich.",
    },
    {
      key: "features.rollout_budget.limit_tokens",
      type: "integer",
      description:
        "Positives Token-Limit für die Nachverfolgung des Rollout-Budgets. Erforderlich, wenn das Rollout-Budget aktiviert ist.",
    },
    {
      key: "features.rollout_budget.reminder_interval_tokens",
      type: "integer",
      description:
        "Positives Token-Intervall zwischen Erinnerungen zum Rollout-Budget. Der Standardwert beträgt 10 % von `limit_tokens`, mindestens jedoch 1 Token.",
    },
    {
      key: "features.rollout_budget.sampling_token_weight",
      type: "number",
      description:
        "Endlicher, nicht negativer Multiplikator für per Sampling erzeugte Token bei der Berechnung des Rollout-Budgets. Standardwert ist `1.0`.",
    },
    {
      key: "features.rollout_budget.prefill_token_weight",
      type: "number",
      description:
        "Endlicher, nicht negativer Multiplikator für Prefill-Token bei der Berechnung des Rollout-Budgets. Standardwert ist `1.0`.",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "Direkt in `config.toml` konfigurierte Lifecycle-Hooks. Sie verwenden dasselbe Ereignisschema wie `hooks.json`. Beispiele und unterstützte Ereignisse findest du im Leitfaden zu Hooks.",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "Matcher-Gruppen für Hook-Ereignisse wie `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `SessionStart`, `SessionEnd`, `SubagentStart`, `SubagentStop`, `UserPromptSubmit`, `Stop` oder `Interrupt`.",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "Hook-Handler für eine Matcher-Gruppe. Befehls-Hooks und Hooks für MCP-Tools werden unterstützt; Handler für Prompt- und Agenten-Hooks werden geparst, aber übersprungen.",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "Einen Befehls-Hook im Hintergrund ausführen, ohne den auslösenden Vorgang zu verzögern. Standardwert ist `false`; `SessionEnd` wird immer synchron ausgeführt. Siehe [Hooks im Hintergrund ausführen](/codex/hooks#run-hooks-in-the-background).",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "Ungefährer Token-Schwellenwert pro Handler, ab dem zu umfangreiche Inhalte von `additionalContext` auf dem Datenträger gespeichert werden und dem Modell eine kürzere Vorschau angezeigt wird. Standardwert ist `2500`; bei `0` wird der vollständige Kontext direkt an das Modell übergeben. Siehe [Große Hook-Ausgaben](/codex/hooks#large-hook-output).",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "Abweichender Befehl für Befehls-Hooks, der nur unter Windows verwendet wird. Der TOML-Alias `command_windows` wird ebenfalls akzeptiert.",
    },
    {
      key: "features.memories",
      type: "boolean",
      description:
        "[Erinnerungen](/codex/customization/memories) aktivieren (standardmäßig deaktiviert).",
    },
    {
      key: "mcp_optional_startup_grace_ms",
      type: "integer (milliseconds)",
      description:
        "Gemeinsame Wartezeit für optionale MCP-Server beim Erstellen des anfänglichen Tool-Katalogs. Standardwert ist `1000`. Setze den Wert auf `0`, um stattdessen für jeden Server dessen `startup_timeout_sec` abzuwarten.",
    },
    {
      key: "mcp_servers.<id>.command",
      type: "string",
      description: "Startbefehl für einen MCP-Server mit stdio.",
    },
    {
      key: "mcp_servers.<id>.args",
      type: "array<string>",
      description: "Argumente, die an den Befehl des MCP-Servers mit stdio übergeben werden.",
    },
    {
      key: "mcp_servers.<id>.env",
      type: "map<string,string>",
      description: "Umgebungsvariablen, die an den MCP-Server mit stdio weitergeleitet werden.",
    },
    {
      key: "mcp_servers.<id>.env_vars",
      type: 'array<string | { name = string, source = "local" | "remote" }>',
      description:
        "Zusätzliche Umgebungsvariablen für die Zulassungsliste eines MCP-Servers mit stdio. Für Zeichenfolgeneinträge gilt standardmäßig `source = \"local\"`; verwende `source = \"remote\"` nur für stdio, das über einen Executor remote ausgeführt wird.",
    },
    {
      key: "mcp_servers.<id>.cwd",
      type: "string",
      description: "Arbeitsverzeichnis für den Prozess des MCP-Servers mit stdio.",
    },
    {
      key: "mcp_servers.<id>.url",
      type: "string",
      description: "Endpunkt für einen MCP-Server mit Streamable HTTP.",
    },
    {
      key: "mcp_servers.<id>.auth",
      type: "oauth | chatgpt",
      description:
        "Fallback für die Authentifizierung eines MCP-HTTP-Servers, nachdem konfigurierte Bearer-Token und Autorisierungsheader geprüft wurden. `oauth` (Standard) verwendet gespeicherte MCP-OAuth-Anmeldedaten, sofern vorhanden. `chatgpt` verwendet für den vertrauenswürdigen, ChatGPT-eigenen Origin die aktuelle ChatGPT-Sitzung und greift bei Bedarf auf gespeicherte OAuth-Anmeldedaten zurück. In beiden Modi ist auch eine Verbindung ohne Authentifizierung möglich, wenn keine Quelle Anmeldedaten liefert.",
    },
    {
      key: "mcp_servers.<id>.oauth.client_id",
      type: "string",
      description:
        "Vorab registrierte OAuth-Client-ID, die für die Autorisierung und den Token-Austausch mit diesem MCP-Server verwendet wird.",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_url",
      type: "string",
      description:
        "Serverspezifischer OAuth-Callback. Vorab registrierte Clients verwenden ihn wieder, wenn die Identifizierung des Ausstellers unterstützt wird oder die URL bereits mit der serverspezifischen Callback-ID endet. Andernfalls verwendet Codex den globalen oder den Standard-Callback und hängt diese ID an. Clients ohne vorab registrierte ID verwenden diesen Callback bei der Client-Registrierung.",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_port",
      type: "integer",
      description:
        "Fester Listener-Port für OAuth-Callbacks dieses MCP-Servers. Überschreibt `mcp_oauth_callback_port`. Konfiguriere für einen direkten Loopback-Callback mit expliziter Portangabe in der URL denselben Listener-Port.",
    },
    {
      key: "mcp_servers.<id>.bearer_token_env_var",
      type: "string",
      description:
        "Umgebungsvariable, aus der das Bearer-Token für einen MCP-HTTP-Server bezogen wird.",
    },
    {
      key: "mcp_servers.<id>.http_headers",
      type: "map<string,string>",
      description: "Statische HTTP-Header, die jeder MCP-HTTP-Anfrage hinzugefügt werden.",
    },
    {
      key: "mcp_servers.<id>.http_headers_helper",
      type: "string (command)",
      description:
        "Lokaler Befehl, der ein JSON-Objekt mit Namen und Werten von HTTP-Headern ausgibt. Wird nur für lokal verbundene MCP-HTTP-Server unterstützt. Explizite Bearer-Token und OAuth-Anmeldedaten haben Vorrang vor Authorization-Headern, die das Hilfsprogramm bereitstellt.",
    },
    {
      key: "mcp_servers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "HTTP-Header für einen MCP-HTTP-Server, deren Werte aus Umgebungsvariablen stammen.",
    },
    {
      key: "mcp_servers.<id>.enabled",
      type: "boolean",
      description: "Einen MCP-Server deaktivieren, ohne seine Konfiguration zu entfernen.",
    },
    {
      key: "mcp_servers.<id>.required",
      type: "boolean",
      description:
        "Wenn true festgelegt ist, schlägt der Start oder die Fortsetzung fehl, falls dieser aktivierte MCP-Server nicht initialisiert werden kann.",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_sec",
      type: "number",
      description:
        "Den standardmäßigen Start-Timeout von 10 s für einen MCP-Server überschreiben.",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_ms",
      type: "number",
      description: "Alias für `startup_timeout_sec` in Millisekunden.",
    },
    {
      key: "mcp_servers.<id>.tool_timeout_sec",
      type: "number",
      description:
        "Den standardmäßigen Timeout von 60 s pro Tool für einen MCP-Server überschreiben.",
    },
    {
      key: "mcp_servers.<id>.enabled_tools",
      type: "array<string>",
      description: "Zulassungsliste der Tool-Namen, die der MCP-Server bereitstellt.",
    },
    {
      key: "mcp_servers.<id>.disabled_tools",
      type: "array<string>",
      description:
        "Sperrliste für den MCP-Server, die nach `enabled_tools` angewendet wird.",
    },
    {
      key: "mcp_servers.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Standardmäßiges Genehmigungsverhalten für MCP-Tools auf diesem Server, sofern für das jeweilige Tool keine abweichende Einstellung vorliegt.",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Abweichendes Genehmigungsverhalten für ein einzelnes MCP-Tool auf diesem Server.",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.output_token_limit",
      type: "integer (positive)",
      description:
        "Token-Budget für die Ausgabe eines einzelnen MCP-Tools, bevor der standardmäßige Aufschlag von 20 % für die Serialisierung hinzukommt. Überschreibt für dieses Tool das standardmäßige Budget des Modells für die Ausgabekürzung.",
    },
    {
      key: "mcp_servers.<id>.scopes",
      type: "array<string>",
      description:
        "OAuth-Berechtigungsbereiche, die bei der Authentifizierung bei diesem MCP-Server angefordert werden.",
    },
    {
      key: "mcp_servers.<id>.oauth_resource",
      type: "string",
      description:
        "Optionaler OAuth-Ressourcenparameter gemäß RFC 8707, der bei der MCP-Anmeldung mitgesendet wird.",
    },
    {
      key: "mcp_servers.<id>.experimental_environment",
      type: "local | remote",
      description:
        "Experimenteller Ausführungsort für einen MCP-Server. `remote` startet stdio-Server über eine Remote-Executor-Umgebung; die Remote-Ausführung von Servern mit Streamable HTTP ist nicht implementiert.",
    },
    {
      key: "agents",
      type: "table",
      description:
        "Einstellungen für mehrere Agenten und Deklarationen benutzerdefinierter Rollen. Namen skalarer Einstellungen sind reserviert und können nicht als benutzerdefinierte Rollennamen verwendet werden.",
    },
    {
      key: "agents.enabled",
      type: "boolean",
      description: "Tools für mehrere Agenten aktivieren oder deaktivieren (Standard: true).",
    },
    {
      key: "agents.max_concurrent_threads_per_session",
      type: "number",
      description:
        "Maximale Anzahl an Threads gestarteter Agenten, die gleichzeitig geöffnet sein können. Der Haupt-Thread zählt nicht mit. Ist kein Wert festgelegt, wählt Codex den Standardwert.",
    },
    {
      key: "agents.max_threads",
      type: "number",
      description:
        "Älterer Alias für `agents.max_concurrent_threads_per_session`.",
    },
    {
      key: "agents.default_subagent_model",
      type: "string",
      description:
        "Standardmodell für gestartete Agenten. Ein beim Starten explizit angegebenes Modell hat Vorrang.",
    },
    {
      key: "agents.default_subagent_reasoning_effort",
      type: "string",
      description:
        "Standardmäßiger Reasoning-Aufwand für gestartete Agenten. Ein beim Starten explizit angegebener Reasoning-Aufwand hat Vorrang.",
    },
    {
      key: "agents.interrupt_message",
      type: "boolean",
      description:
        "Eine für das Modell sichtbare Nachricht aufzeichnen, wenn ein Agenten-Turn unterbrochen wird (Standard: true).",
    },
    {
      key: "agents.<name>.description",
      type: "string",
      description:
        "Hinweise zur Rolle, die Codex beim Auswählen und Starten dieses Agententyps angezeigt werden.",
    },
    {
      key: "agents.<name>.config_file",
      type: "string (path)",
      description:
        "Pfad zu einer TOML-Konfigurationsebene für diese Rolle. Relative Pfade werden ausgehend von der Konfigurationsdatei aufgelöst, in der die Rolle deklariert ist.",
    },
    {
      key: "memories.generate_memories",
      type: "boolean",
      description:
        "Wenn `false` festgelegt ist, werden neu erstellte Threads nicht als Eingaben für die Generierung von Erinnerungen gespeichert. Standardwert ist `true`.",
    },
    {
      key: "memories.use_memories",
      type: "boolean",
      description:
        "Wenn `false` festgelegt ist, bindet Codex vorhandene Erinnerungen nicht in zukünftige Sitzungen ein. Standardwert ist `true`.",
    },
    {
      key: "memories.disable_on_external_context",
      type: "boolean",
      description:
        "Bei `true` werden Threads, die externen Kontext wie MCP-Tool-Aufrufe, Websuche oder Tool-Suche verwenden, von der Erstellung von Erinnerungen ausgeschlossen. Standard: `false`. Älterer Alias: `memories.no_memories_if_mcp_or_web_search`.",
    },
    {
      key: "memories.max_raw_memories_for_consolidation",
      type: "number",
      description:
        "Maximale Anzahl neuerer, unverarbeiteter Erinnerungen, die für die globale Konsolidierung aufbewahrt werden. Standard: `256`, begrenzt auf höchstens `4096`.",
    },
    {
      key: "memories.max_unused_days",
      type: "number",
      description:
        "Maximale Anzahl von Tagen seit der letzten Verwendung einer Erinnerung, nach denen sie nicht mehr für die Konsolidierung infrage kommt. Standard: `30`, begrenzt auf den Bereich von `0` bis `365`.",
    },
    {
      key: "memories.max_rollout_age_days",
      type: "number",
      description:
        "Maximales Alter der Threads, die für die Erstellung von Erinnerungen berücksichtigt werden. Standard: `30`, begrenzt auf den Bereich von `0` bis `90`.",
    },
    {
      key: "memories.max_rollouts_per_startup",
      type: "number",
      description:
        "Maximale Anzahl von Rollout-Kandidaten, die pro Startdurchlauf verarbeitet werden. Standard: `16`, begrenzt auf höchstens `128`.",
    },
    {
      key: "memories.min_rollout_idle_hours",
      type: "number",
      description:
        "Mindestdauer der Inaktivität, bevor ein Thread für die Erstellung von Erinnerungen berücksichtigt wird. Standard: `6`, begrenzt auf den Bereich von `1` bis `48`.",
    },
    {
      key: "memories.min_rate_limit_remaining_percent",
      type: "number",
      description:
        "Prozentualer Anteil, der in den Ratenlimit-Zeitfenstern von Codex mindestens verfügbar sein muss, bevor die Erstellung von Erinnerungen beginnt. Standard: `25`, begrenzt auf den Bereich von `0` bis `100`.",
    },
    {
      key: "memories.extract_model",
      type: "string",
      description: "Optionale abweichende Modellauswahl für die Extraktion von Erinnerungen aus einzelnen Threads.",
    },
    {
      key: "memories.consolidation_model",
      type: "string",
      description: "Optionale abweichende Modellauswahl für die globale Konsolidierung von Erinnerungen.",
    },
    {
      key: "features.unified_exec",
      type: "boolean",
      description:
        "Das vereinheitlichte PTY-basierte exec-Tool verwenden (stabil; außer auf Windows standardmäßig aktiviert).",
    },
    {
      key: "features.shell_snapshot",
      type: "boolean",
      description:
        "Einen Snapshot der Shell-Umgebung erstellen, um wiederholte Befehle zu beschleunigen (stabil; standardmäßig aktiviert).",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description:
        "Tools für die Zusammenarbeit mehrerer Agenten aktivieren (`spawn_agent`, `send_input`, `resume_agent`, `wait_agent` und `close_agent`) (stabil; standardmäßig aktiviert).",
    },
    {
      key: "features.goals",
      type: "boolean",
      description:
        "Dauerhaft gespeicherte Ziele und automatische Fortsetzung aktivieren (stabil; standardmäßig aktiviert).",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description: "Remote-Katalog für Plug-ins aktivieren (stabil; standardmäßig aktiviert).",
    },
    {
      key: "features.personality",
      type: "boolean",
      description:
        "Bedienelemente zur Auswahl der Persönlichkeit aktivieren (stabil; standardmäßig aktiviert).",
    },
    {
      key: "features.network_proxy",
      type: "boolean | table",
      description:
        "Netzwerk-Proxy für Befehle in der Sandbox starten (experimentell; standardmäßig deaktiviert). Er ist erforderlich, um die Domainregeln der Berechtigungsprofile durchzusetzen, sofern der Proxy nicht durch aktivierte, administrativ verwaltete `experimental_network`-Anforderungen gestartet wird. Verwende die Tabellenform, wenn du Richtlinienoptionen auf Funktionsebene wie `domains` festlegst. Filtert weder die Websuche noch Apps, MCP oder andere gehostete Tools.",
    },
    {
      key: "features.network_proxy.enabled",
      type: "boolean",
      description:
        "Netzwerk-Proxy für Befehle in der Sandbox starten, wenn der Netzwerkzugriff für Befehle aktiviert ist. Standard: `false`. Solange der Proxy deaktiviert ist, werden die Domainregeln der Berechtigungsprofile nicht durchgesetzt.",
    },
    {
      key: "features.network_proxy.domains",
      type: "map<string, allow | deny>",
      description:
        "Domainrichtlinie für den Netzwerkzugriff in der Sandbox. Standardmäßig nicht festgelegt; externe Ziele sind erst zulässig, wenn du Regeln mit `allow` hinzufügst. Unterstützt exakt angegebene Hosts, `*.example.com` ausschließlich für Subdomains, `**.example.com` für die Apex-Domain einschließlich ihrer Subdomains sowie globale Zulassungsregeln mit `*`. Bevorzuge Regeln mit begrenztem Geltungsbereich, da `*` ausgehenden Zugriff auf öffentliche Ziele umfassend freigibt. Füge für gesperrte Ziele Regeln mit `deny` hinzu; bei Konflikten hat `deny` Vorrang.",
    },
    {
      key: "features.network_proxy.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "Unix-Socket-Richtlinie für den Netzwerkzugriff in der Sandbox. Standardmäßig nicht festgelegt; füge für zulässige Sockets Einträge mit `allow` hinzu.",
    },
    {
      key: "features.network_proxy.allow_local_binding",
      type: "boolean",
      description:
        "Umfassenderen Zugriff auf lokale oder private Netzwerke zulassen. Standard: `false`; Zulassungsregeln für eine exakt angegebene lokale IP-Adresse oder für `localhost` können bestimmte lokale Ziele weiterhin freigeben.",
    },
    {
      key: "features.network_proxy.enable_socks5",
      type: "boolean",
      description: "SOCKS5-Unterstützung bereitstellen. Standard: `true`.",
    },
    {
      key: "features.network_proxy.enable_socks5_udp",
      type: "boolean",
      description: "UDP über SOCKS5 zulassen. Standard: `true`.",
    },
    {
      key: "features.network_proxy.allow_upstream_proxy",
      type: "boolean",
      description:
        "Verkettung mit einem in der Umgebung konfigurierten Upstream-Proxy zulassen. Standard: `true`.",
    },
    {
      key: "features.network_proxy.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "Listener-Adressen zulassen, die keine Loopback-Adressen sind. Standard: `false`; bei Aktivierung können Proxy-Listener auch außerhalb von localhost erreichbar werden.",
    },
    {
      key: "features.network_proxy.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "Beliebige Unix-Socket-Ziele zulassen, statt den Zugriff auf eine Allowlist zu beschränken. Standard: `false`; nur in streng kontrollierten Umgebungen verwenden.",
    },
    {
      key: "features.network_proxy.proxy_url",
      type: "string",
      description:
        "HTTP-Listener-URL für den Netzwerkzugriff in der Sandbox. Standard: `\"http://127.0.0.1:3128\"`.",
    },
    {
      key: "features.network_proxy.socks_url",
      type: "string",
      description:
        "SOCKS5-Listener-URL. Standard: `\"http://127.0.0.1:8081\"`.",
    },
    {
      key: "features.web_search",
      type: "boolean",
      description:
        "Veralteter Schalter aus älteren Versionen; verwende vorzugsweise die Einstellung `web_search` auf oberster Ebene.",
    },
    {
      key: "features.web_search_cached",
      type: "boolean",
      description:
        "Veralteter Schalter aus älteren Versionen. Ist `web_search` nicht festgelegt, entspricht true der Einstellung `web_search = \"cached\"`.",
    },
    {
      key: "features.web_search_request",
      type: "boolean",
      description:
        "Veralteter Schalter aus älteren Versionen. Ist `web_search` nicht festgelegt, entspricht true der Einstellung `web_search = \"live\"`.",
    },
    {
      key: "features.shell_tool",
      type: "boolean",
      description:
        "Das standardmäßige Tool `shell` zum Ausführen von Befehlen aktivieren (stabil; standardmäßig aktiviert).",
    },
    {
      key: "features.enable_request_compression",
      type: "boolean",
      description:
        "Anfragekörper von Streaming-Anfragen mit zstd komprimieren, sofern dies unterstützt wird (stabil; standardmäßig aktiviert).",
    },
    {
      key: "features.skill_mcp_dependency_install",
      type: "boolean",
      description:
        "Installationsaufforderungen und die Installation fehlender MCP-Abhängigkeiten für Skills zulassen (stabil; standardmäßig aktiviert).",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "Die Auswahl der Servicestufe aus dem Modellkatalog in der TUI aktivieren, einschließlich der Befehle für die Fast-Servicestufe, sofern das aktive Modell sie anbietet (stabil; standardmäßig aktiviert).",
    },
    {
      key: "features.prevent_idle_sleep",
      type: "boolean",
      description:
        "Verhindern, dass der Computer während einer laufenden Interaktion in den Ruhezustand wechselt (experimentell; standardmäßig deaktiviert).",
    },
    {
      key: "suppress_unstable_features_warning",
      type: "boolean",
      description:
        "Die Warnung unterdrücken, die bei aktivierten Feature-Flags für noch in Entwicklung befindliche Funktionen angezeigt wird.",
    },
    {
      key: "model_providers.<id>",
      type: "table",
      description:
        "Definition eines benutzerdefinierten Anbieters. Die IDs der integrierten Anbieter (`openai`, `ollama` und `lmstudio`) sind reserviert und können nicht überschrieben werden.",
    },
    {
      key: "model_providers.<id>.name",
      type: "string",
      description: "Anzeigename eines benutzerdefinierten Modellanbieters.",
    },
    {
      key: "model_providers.<id>.base_url",
      type: "string",
      description: "API-Basis-URL des Modellanbieters.",
    },
    {
      key: "model_providers.<id>.env_key",
      type: "string",
      description: "Umgebungsvariable, die den API-Schlüssel des Anbieters bereitstellt.",
    },
    {
      key: "model_providers.<id>.env_key_instructions",
      type: "string",
      description: "Optionale Hinweise zum Einrichten des API-Schlüssels des Anbieters.",
    },
    {
      key: "model_providers.<id>.experimental_bearer_token",
      type: "string",
      description:
        "Direktes Bearer-Token für den Anbieter (nicht empfohlen; verwende `env_key`).",
    },
    {
      key: "model_providers.<id>.requires_openai_auth",
      type: "boolean",
      description:
        "Der Anbieter verwendet die OpenAI-Authentifizierung (Standard: false).",
    },
    {
      key: "model_providers.<id>.wire_api",
      type: "responses",
      description:
        "Vom Anbieter verwendetes Protokoll. `responses` ist der einzige unterstützte Wert und wird standardmäßig verwendet, wenn die Angabe fehlt.",
    },
    {
      key: "model_providers.<id>.query_params",
      type: "map<string,string>",
      description: "Zusätzliche Abfrageparameter, die an Anfragen an den Anbieter angehängt werden.",
    },
    {
      key: "model_providers.<id>.http_headers",
      type: "map<string,string>",
      description: "Statische HTTP-Header, die Anfragen an den Anbieter hinzugefügt werden.",
    },
    {
      key: "model_providers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "HTTP-Header, deren Werte aus vorhandenen Umgebungsvariablen übernommen werden.",
    },
    {
      key: "model_providers.<id>.request_max_retries",
      type: "number",
      description:
        "Anzahl der Wiederholungsversuche für HTTP-Anfragen an den Anbieter (Standard: 4).",
    },
    {
      key: "model_providers.<id>.stream_max_retries",
      type: "number",
      description: "Anzahl der Wiederholungsversuche nach Unterbrechungen von SSE-Streams (Standard: 5).",
    },
    {
      key: "model_providers.<id>.stream_idle_timeout_ms",
      type: "number",
      description:
        "Leerlauf-Timeout für SSE-Streams in Millisekunden (Standard: 300000).",
    },
    {
      key: "model_providers.<id>.supports_websockets",
      type: "boolean",
      description:
        "Gibt an, ob dieser Anbieter den WebSocket-Transport der Responses API unterstützt.",
    },
    {
      key: "model_providers.<id>.supports_standalone_web_search",
      type: "boolean",
      description:
        "Unterstützung für einen kompatiblen, eigenständigen Endpunkt für die Websuche angeben (Standard: false). Die eigenständige Suche ist weiterhin in Entwicklung und standardmäßig deaktiviert. Die Kompatibilität des Anbieters allein aktiviert sie nicht.",
    },
    {
      key: "model_providers.<id>.auth",
      type: "table",
      description:
        "Konfiguration für einen benutzerdefinierten Anbieter, bei der ein Befehl das Bearer-Token bereitstellt. Nicht zusammen mit `env_key`, `experimental_bearer_token` oder `requires_openai_auth` verwenden.",
    },
    {
      key: "model_providers.<id>.auth.command",
      type: "string",
      description:
        "Befehl, der ausgeführt wird, wenn Codex ein Bearer-Token benötigt. Der Befehl muss das Token auf stdout ausgeben.",
    },
    {
      key: "model_providers.<id>.auth.args",
      type: "array<string>",
      description: "Argumente, die an den Token-Befehl übergeben werden.",
    },
    {
      key: "model_providers.<id>.auth.timeout_ms",
      type: "number",
      description:
        "Maximale Laufzeit des Token-Befehls in Millisekunden (Standard: 5000).",
    },
    {
      key: "model_providers.<id>.auth.refresh_interval_ms",
      type: "number",
      description:
        "Intervall in Millisekunden, in dem Codex das Token proaktiv aktualisiert (Standard: 300000). Setze den Wert auf `0`, um das Token nur nach einem erneuten Authentifizierungsversuch zu aktualisieren.",
    },
    {
      key: "model_providers.<id>.auth.cwd",
      type: "string (path)",
      description: "Arbeitsverzeichnis für den Token-Befehl.",
    },
    {
      key: "model_providers.amazon-bedrock.aws.profile",
      type: "string",
      description:
        "AWS-Profilname, den der integrierte Anbieter `amazon-bedrock` verwendet.",
    },
    {
      key: "model_providers.amazon-bedrock.aws.region",
      type: "string",
      description: "AWS-Region, die der integrierte Anbieter `amazon-bedrock` verwendet.",
    },
    {
      key: "model_reasoning_effort",
      type: "minimal | low | medium | high | xhigh",
      description:
        "Den Reasoning-Aufwand für unterstützte Modelle anpassen (nur Responses API; `xhigh` ist modellabhängig).",
    },
    {
      key: "plan_mode_reasoning_effort",
      type: "none | minimal | low | medium | high | xhigh",
      description:
        "Abweichende Einstellung des Reasoning-Aufwands speziell für den Planmodus. Ist kein Wert festgelegt, verwendet der Planmodus seine integrierte Standardeinstellung.",
    },
    {
      key: "model_reasoning_summary",
      type: "auto | concise | detailed | none",
      description:
        "Detailgrad der Reasoning-Zusammenfassungen auswählen oder Zusammenfassungen vollständig deaktivieren.",
    },
    {
      key: "model_verbosity",
      type: "low | medium | high",
      description:
        "Optionale abweichende Einstellung für die Ausführlichkeit von GPT-5 über die Responses API. Ist kein Wert festgelegt, wird die Standardeinstellung des ausgewählten Modells oder Presets verwendet.",
    },
    {
      key: "model_supports_reasoning_summaries",
      type: "boolean",
      description: "Erzwingen, dass Codex Reasoning-Metadaten sendet oder nicht sendet.",
    },
    {
      key: "shell_environment_policy.inherit",
      type: "all | core | none",
      description:
        "Grundlegende Vererbung von Umgebungsvariablen beim Starten von Unterprozessen.",
    },
    {
      key: "shell_environment_policy.ignore_default_excludes",
      type: "boolean",
      description:
        "Variablen beibehalten, deren Namen KEY, SECRET oder TOKEN enthalten, bevor andere Filter angewendet werden (Standard: true). Auf false setzen, um Variablen anhand typischer Geheimnisnamen automatisch auszuschließen.",
    },
    {
      key: "shell_environment_policy.filters",
      type: "map<string, include | exclude>",
      description:
        "Kanonische Musterfilter für Umgebungsvariablen, die Groß- und Kleinschreibung ignorieren. Einschließende Einträge bilden eine Zulassungsliste und können ausgeschlossene Werte nicht wiederherstellen. Explizite `set`-Werte werden nach den Ausschlüssen angewendet. Kombiniere Filter nicht mit älteren `exclude`- oder `include_only`-Arrays in derselben Konfigurationsebene.",
    },
    {
      key: "shell_environment_policy.exclude",
      type: "array<string>",
      description:
        "Ältere Ausschlussmuster für Umgebungsvariablen. Verwende für neue Konfigurationen `shell_environment_policy.filters`; kombiniere nicht beide Formen in derselben Konfigurationsebene.",
    },
    {
      key: "shell_environment_policy.include_only",
      type: "array<string>",
      description:
        "Ältere Zulassungsliste mit Mustern für Umgebungsvariablen. Verwende für neue Konfigurationen `shell_environment_policy.filters`; kombiniere nicht beide Formen in derselben Konfigurationsebene.",
    },
    {
      key: "shell_environment_policy.set",
      type: "map<string,string>",
      description:
        "Explizite Umgebungswerte, die nach den Ausschlüssen eingefügt werden; einschließende Filter können sie weiterhin entfernen.",
    },
    {
      key: "shell_environment_policy.experimental_use_profile",
      type: "boolean",
      description: "Beim Starten von Unterprozessen das Shell-Profil des Benutzerkontos verwenden.",
    },
    {
      key: "project_root_markers",
      type: "array<string>",
      description:
        "Liste der Dateinamen, die das Projektstammverzeichnis kennzeichnen; wird bei der Suche nach dem Projektstammverzeichnis in übergeordneten Verzeichnissen verwendet.",
    },
    {
      key: "project_doc_max_bytes",
      type: "number",
      description:
        "Maximale Anzahl an Bytes, die beim Zusammenstellen der Projektanweisungen aus `AGENTS.md` gelesen werden.",
    },
    {
      key: "project_doc_fallback_filenames",
      type: "array<string>",
      description: "Zusätzliche Dateinamen, nach denen gesucht wird, wenn `AGENTS.md` fehlt.",
    },
    {
      key: "history.persistence",
      type: "save-all | none",
      description:
        "Festlegen, ob Codex Sitzungsprotokolle in history.jsonl speichert.",
    },
    {
      key: "tool_output_token_limit",
      type: "number",
      description:
        "Token-Budget zum Speichern einzelner Tool- oder Funktionsausgaben im Verlauf.",
    },
    {
      key: "background_terminal_max_timeout",
      type: "number",
      description:
        "Maximales Abfragezeitfenster in Millisekunden für leere `write_stdin`-Abfragen (Abfragen des Hintergrundterminals). Standard: `300000` (5 Minuten). Ersetzt den älteren Schlüssel `background_terminal_timeout`.",
    },
    {
      key: "history.max_bytes",
      type: "number",
      description:
        "Begrenzt, sofern festgelegt, die Größe der Verlaufsdatei in Byte, indem die ältesten Einträge entfernt werden.",
    },
    {
      key: "file_opener",
      type: "vscode | vscode-insiders | windsurf | cursor | none",
      description:
        "URI-Schema zum Öffnen von Quellenverweisen aus der Codex-Ausgabe (Standard: `vscode`).",
    },
    {
      key: "otel.environment",
      type: "string",
      description:
        "Umgebungs-Tag für ausgegebene OpenTelemetry-Ereignisse (Standard: `dev`).",
    },
    {
      key: "otel.exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "OpenTelemetry-Exporter auswählen und gegebenenfalls Endpunktmetadaten angeben.",
    },
    {
      key: "otel.trace_exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "OpenTelemetry-Trace-Exporter auswählen und gegebenenfalls Endpunktmetadaten angeben.",
    },
    {
      key: "otel.metrics_exporter",
      type: "none | statsig | otlp-http | otlp-grpc",
      description:
        "OpenTelemetry-Metrik-Exporter auswählen (Standard: `statsig`).",
    },
    {
      key: "otel.log_user_prompt",
      type: "boolean",
      description:
        "Export unverarbeiteter Prompts von Nutzenden zusammen mit OpenTelemetry-Logs aktivieren.",
    },
    {
      key: "otel.exporter.<id>.endpoint",
      type: "string",
      description: "Exporter-Endpunkt für OTEL-Logs.",
    },
    {
      key: "otel.exporter.<id>.protocol",
      type: "binary | json",
      description: "Vom OTLP/HTTP-Exporter verwendetes Protokoll.",
    },
    {
      key: "otel.exporter.<id>.headers",
      type: "map<string,string>",
      description: "Statische Header, die in Anfragen des OTEL-Exporters enthalten sind.",
    },
    {
      key: "otel.trace_exporter.<id>.endpoint",
      type: "string",
      description: "Endpunkt des Trace-Exporters für OTEL-Logs.",
    },
    {
      key: "otel.trace_exporter.<id>.protocol",
      type: "binary | json",
      description: "Vom OTLP/HTTP-Trace-Exporter verwendetes Protokoll.",
    },
    {
      key: "otel.trace_exporter.<id>.headers",
      type: "map<string,string>",
      description: "Statische Header, die in Anfragen des OTEL-Trace-Exporters enthalten sind.",
    },
    {
      key: "otel.exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "Pfad zum CA-Zertifikat für die TLS-Verbindung des OTEL-Exporters.",
    },
    {
      key: "otel.exporter.<id>.tls.client-certificate",
      type: "string",
      description: "Pfad zum Clientzertifikat für die TLS-Verbindung des OTEL-Exporters.",
    },
    {
      key: "otel.exporter.<id>.tls.client-private-key",
      type: "string",
      description: "Pfad zum privaten Clientschlüssel für die TLS-Verbindung des OTEL-Exporters.",
    },
    {
      key: "otel.trace_exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "Pfad zum CA-Zertifikat für die TLS-Verbindung des OTEL-Trace-Exporters.",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-certificate",
      type: "string",
      description: "Pfad zum Clientzertifikat für die TLS-Verbindung des OTEL-Trace-Exporters.",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-private-key",
      type: "string",
      description: "Pfad zum privaten Clientschlüssel für die TLS-Verbindung des OTEL-Trace-Exporters.",
    },
    {
      key: "desktop.custom_file_handlers.<id>",
      type: "table",
      description:
        "Nur auf Benutzerebene. Definiert für die ChatGPT-Desktop-App ein zusätzliches Ziel im Menü **Öffnen in**. Beispiele und Einschränkungen für Handler-IDs findest du unter [Benutzerdefinierte Dateihandler hinzufügen](/codex/config-file/config-advanced#add-custom-file-handlers).",
    },
    {
      key: "desktop.custom_file_handlers.<id>.label",
      type: "string",
      description: "Anzeigename in den Menüs **Öffnen in**. Erforderlich.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.icon",
      type: "string",
      description:
        "Pfad zu einem mitgelieferten Asset, Base64-codierte URL im Format `data:image/...`, Datei-URI oder absoluter lokaler Pfad für das Handler-Symbol. Erforderlich; bei nicht unterstützten Quellen wird das Standardsymbol von VS Code verwendet.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.command",
      type: "string",
      description:
        "Pfad zur ausführbaren Datei oder Befehlsname, um das Programm zu erkennen und zu starten. Erforderlich.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.args",
      type: "array<string>",
      description:
        "Argumente, die zwischen Befehl und Dateieingabe eingefügt werden (Standard: `[]`).",
    },
    {
      key: "desktop.custom_file_handlers.<id>.input",
      type: "path | json_argument | json_stdin",
      description:
        "Legt fest, wie die App Dateieingaben an den Handler sendet (Standard: `path`).",
    },
    {
      key: "desktop.custom_file_handlers.<id>.supports_ssh",
      type: "boolean",
      description:
        "Handler für Dateien in SSH-Workspaces anbieten (Standard: `false`).",
    },
    {
      key: "tui",
      type: "table",
      description:
        "TUI-spezifische Optionen, beispielsweise zum Aktivieren von Inline-Desktop-Benachrichtigungen.",
    },
    {
      key: "tui.notifications",
      type: "boolean | array<string>",
      description:
        "TUI-Benachrichtigungen aktivieren und optional auf bestimmte Ereignistypen beschränken.",
    },
    {
      key: "tui.notification_method",
      type: "auto | osc9 | bel",
      description:
        "Methode für Terminalbenachrichtigungen (Standard: auto).",
    },
    {
      key: "tui.notification_condition",
      type: "unfocused | always",
      description:
        "Legt fest, ob TUI-Benachrichtigungen nur bei nicht fokussiertem Terminal oder unabhängig vom Fokus ausgelöst werden. Standard: `unfocused`.",
    },
    {
      key: "tui.animations",
      type: "boolean",
      description:
        "Terminalanimationen (Willkommensbildschirm, Schimmereffekt, rotierender Ladeindikator) aktivieren (Standard: true).",
    },
    {
      key: "tui.alternate_screen",
      type: "auto | always | never",
      description:
        "Nutzung des alternativen Bildschirmpuffers für die TUI steuern (Standard: auto; bei auto wird er in Zellij nicht verwendet, damit der Scrollback-Verlauf erhalten bleibt).",
    },
    {
      key: "tui.resume_cwd",
      type: "current | session",
      description:
        "Arbeitsverzeichnis für das Fortsetzen oder Forken einer Sitzung. Ist kein Wert festgelegt und unterscheidet sich dein aktuelles Verzeichnis vom gespeicherten Verzeichnis der Sitzung, fordert Codex dich zur Auswahl auf.",
    },
    {
      key: "tui.vim_mode_default",
      type: "boolean",
      description:
        "Den Editor im Vim-Normalmodus statt im Einfügemodus starten (Standard: false). Du kannst den Modus weiterhin pro Sitzung mit `/vim` umschalten.",
    },
    {
      key: "tui.raw_output_mode",
      type: "boolean",
      description:
        "Die TUI im Raw-Scrollback-Modus starten, um Text bequem im Terminal auswählen und kopieren zu können (Standard: false). Du kannst den Modus mit `/raw` oder der Standard-Tastenkombination `alt-r` umschalten.",
    },
    {
      key: "tui.show_tooltips",
      type: "boolean",
      description:
        "Tooltips für den Einstieg auf dem Willkommensbildschirm der TUI anzeigen (Standard: true).",
    },
    {
      key: "tui.status_line",
      type: "array<string> | null",
      description:
        "Geordnete Liste der Elementkennungen für die Statuszeile in der TUI-Fußzeile. `null` deaktiviert die Statuszeile.",
    },
    {
      key: "tui.terminal_title",
      type: "array<string> | null",
      description:
        "Geordnete Liste der Elementkennungen für den Titel des Terminalfensters oder -Tabs. Standard: `[\"spinner\", \"project\"]`; `null` deaktiviert Titelaktualisierungen.",
    },
    {
      key: "tui.theme",
      type: "string",
      description:
        "Theme für die Syntaxhervorhebung überschreiben (Theme-Name in Kebab-Case).",
    },
    {
      key: "tui.keymap.<context>.<action>",
      type: "string | array<string>",
      description:
        "Tastenkombination für eine TUI-Aktion. Unterstützte Kontexte sind unter anderem `global`, `chat`, `composer`, `editor`, `vim_normal`, `vim_operator`, `vim_text_object`, `pager`, `list` und `approval`. Bestimmte Aktionen im Editor greifen ersatzweise auf passende Belegungen in `tui.keymap.global` zurück; kontextspezifische Belegungen haben Vorrang, wenn sie unterstützt werden.",
    },
    {
      key: "tui.keymap.<context>.<action> = []",
      type: "empty array",
      description:
        "Tastenbelegung für die Aktion in diesem Belegungskontext entfernen. Tastennamen werden als normalisierte Zeichenfolgen wie `ctrl-a`, `shift-enter`, `page-down` oder `minus` angegeben.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled",
      type: "boolean",
      description:
        "Einen in einem installierten Plug-in enthaltenen MCP-Server aktivieren oder deaktivieren, ohne das Plug-in-Manifest zu ändern.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Standardmäßiges Genehmigungsverhalten für Tools eines MCP-Servers, den ein Plug-in bereitstellt.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled_tools",
      type: "array<string>",
      description:
        "Zulassungsliste für Tools, die ein MCP-Server aus einem Plug-in bereitstellt.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.disabled_tools",
      type: "array<string>",
      description:
        "Sperrliste für einen MCP-Server aus einem Plug-in, die nach `enabled_tools` angewendet wird.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Überschreibung des Genehmigungsverhaltens für ein einzelnes MCP-Tool aus einem Plug-in.",
    },
    {
      key: "tui.model_availability_nux.<model>",
      type: "integer",
      description: "Interner Status des beim Start angezeigten Tooltips, mit dem Modell-Slug als Schlüssel.",
    },
    {
      key: "hide_agent_reasoning",
      type: "boolean",
      description:
        "Reasoning-Ereignisse sowohl in der TUI als auch in der Ausgabe von `codex exec` unterdrücken.",
    },
    {
      key: "show_raw_agent_reasoning",
      type: "boolean",
      description:
        "Unverarbeitete Reasoning-Inhalte anzeigen, wenn das aktive Modell sie ausgibt.",
    },
    {
      key: "disable_paste_burst",
      type: "boolean",
      description: "Erkennung schneller Eingabefolgen als eingefügten Text in der TUI deaktivieren.",
    },
    {
      key: "windows_wsl_setup_acknowledged",
      type: "boolean",
      description: "Erfasst, ob die Einführung für Windows bestätigt wurde (nur Windows).",
    },
    {
      key: "chatgpt_base_url",
      type: "string",
      description: "Überschreibt die beim ChatGPT-Anmeldevorgang verwendete Basis-URL.",
    },
    {
      key: "cli_auth_credentials_store",
      type: "file | keyring | auto",
      description:
        "Steuert, wo die CLI zwischengespeicherte Zugangsdaten ablegt (in der Datei auth.json oder im Schlüsselbund des Betriebssystems).",
    },
    {
      key: "mcp_oauth_credentials_store",
      type: "auto | file | keyring",
      description: "Bevorzugter Speicherort für MCP-OAuth-Zugangsdaten.",
    },
    {
      key: "mcp_oauth_callback_port",
      type: "integer",
      description:
        "Optionaler globaler, fester Port für den lokalen HTTP-Callback-Server bei der MCP-OAuth-Anmeldung. Ein serverspezifischer `oauth.callback_port` hat Vorrang. Ist keiner der beiden Werte festgelegt, bindet sich Codex an einen vom Betriebssystem gewählten temporären Port.",
    },
    {
      key: "mcp_oauth_callback_url",
      type: "string",
      description:
        "Optionale Callback-Basis-URL für die MCP-OAuth-Anmeldung, etwa die Ingress-URL einer Devbox. Neu hinzugefügte, vorab registrierte Clients verwenden diese URL unverändert, wenn der Autorisierungsserver die Identifizierung des Ausstellers unterstützt. Bestehende Clients ohne gespeicherten Callback hängen eine serverspezifische Callback-ID an. Ohne Unterstützung für die Ausstelleridentifizierung verwendet jeder vorab registrierte MCP-Server, dessen konfiguriertem Callback die erforderliche ID fehlt, ersatzweise diese URL mit angehängter ID. Ports in Callback-URLs legen den Listener-Port nicht fest.",
    },
    {
      key: "experimental_use_unified_exec_tool",
      type: "boolean",
      description:
        "Veralteter Name zum Aktivieren von unified exec. Verwende bevorzugt `[features].unified_exec` oder `codex --enable unified_exec`.",
    },
    {
      key: "tools.web_search",
      type: 'boolean | { context_size = "low|medium|high", allowed_domains = [string], location = { country, region, city, timezone } }',
      description:
        "Optionale Konfiguration des Websuchtools. In der Objektform lassen sich die Größe des Suchkontexts, zulässige Suchdomänen und der ungefähre Standort der nutzenden Person festlegen. Diese Suchdomänenfilter sind von den Netzwerk-Domänenregeln für Befehle in der Sandbox getrennt und schränken Konnektoren oder MCP-Server nicht ein.",
    },
    {
      key: "tools.view_image",
      type: "boolean",
      description: "Aktiviert das Tool `view_image` zum Anhängen lokaler Bilder.",
    },
    {
      key: "web_search",
      type: "disabled | cached | indexed | live",
      description:
        "Modus für die Websuche (Standard: `\"cached\"`; cached verwendet einen von OpenAI gepflegten Index ohne externen Webzugriff; indexed erlaubt externen Zugriff nur, wenn der Suchindex ihn freigibt; bei Verwendung von `--yolo` oder einer anderen Sandbox-Einstellung mit Vollzugriff ist `\"live\"` der Standard). Verwende `\"live\"` für uneingeschränkten Live-Abruf oder `\"disabled\"`, um das Tool zu entfernen.",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "Name des standardmäßigen Berechtigungsprofils für Tool-Aufrufe in der Sandbox. Integrierte Profile sind `:read-only`, `:workspace` und `:danger-full-access`; benutzerdefinierte Profilnamen erfordern passende Tabellen unter `[permissions.<name>]`. Nicht mit `sandbox_mode` oder `[sandbox_workspace_write]` kombinieren.",
    },
    {
      key: "permissions.<name>.description",
      type: "string",
      description:
        "Für Menschen lesbare Beschreibung dieses benannten Profils. Ein Profil erbt die Beschreibung seines übergeordneten Profils nicht über `extends`.",
    },
    {
      key: "permissions.<name>.extends",
      type: "string",
      description:
        "Optionales übergeordnetes Profil, das vor diesem benannten Profil angewendet wird. Gib ein anderes benanntes Profil, `:read-only` oder `:workspace` an. `:danger-full-access`, nicht definierte übergeordnete Profile und Zyklen werden abgelehnt.",
    },
    {
      key: "permissions.<name>.workspace_roots",
      type: "table",
      description:
        "Im Profil definierte Workspace-Stammverzeichnisse, für die ebenso wie für die zur Laufzeit geltenden Workspace-Stammverzeichnisse der Sitzung die Dateisystemregeln für `:workspace_roots` gelten.",
    },
    {
      key: "permissions.<name>.workspace_roots.<path>",
      type: "boolean",
      description:
        "Nimmt bei `true` einen Pfad in die Menge der Workspace-Stammverzeichnisse des Profils auf. Deaktivierte Einträge bleiben inaktiv.",
    },
    {
      key: "permissions.<name>.filesystem",
      type: "table",
      description:
        "Benanntes Berechtigungsprofil für das Dateisystem. Jeder Schlüssel ist ein absoluter Pfad oder ein spezielles Token wie `:minimal` oder `:workspace_roots`.",
    },
    {
      key: "permissions.<name>.filesystem.glob_scan_max_depth",
      type: "number",
      description:
        "Maximale Tiefe beim Auflösen von Glob-Mustern für Leseverbote auf Plattformen, die übereinstimmende Pfade vor dem Start der Sandbox als Momentaufnahme erfassen. Muss bei Angabe mindestens `1` betragen.",
    },
    {
      key: "permissions.<name>.filesystem.<path-or-glob>",
      type: '"read" | "write" | "deny" | table',
      description:
        "Gewährt direkten Zugriff für einen Pfad, ein Glob-Muster oder ein spezielles Token oder legt den Geltungsbereich verschachtelter Einträge unter diesem Stammverzeichnis fest. Verwende `\"deny\"`, um den Lesezugriff auf übereinstimmende Pfade zu verweigern.",
    },
    {
      key: 'permissions.<name>.filesystem.":workspace_roots".<subpath-or-glob>',
      type: '"read" | "write" | "deny"',
      description:
        "Dateisystemzugriff, dessen Geltungsbereich relativ zu jedem effektiven Workspace-Stammverzeichnis festgelegt wird. Verwende `\".\"` für das Stammverzeichnis selbst; bei Glob-Unterpfaden wie `\"**/*.env\"` lässt sich der Lesezugriff mit `\"deny\"` verweigern.",
    },
    {
      key: "permissions.<name>.network.enabled",
      type: "boolean",
      description:
        "Aktiviert den Netzwerkzugriff für Befehle in diesem Berechtigungsprofil. Dadurch wird der Netzwerkproxy nicht gestartet. Ohne `features.network_proxy` oder aktivierte, von der Administration verwaltete Netzwerkanforderungen greifen Befehle direkt auf das Netzwerk zu, und die Domänenregeln des Profils werden nicht durchgesetzt.",
    },
    {
      key: "permissions.<name>.network.proxy_url",
      type: "string",
      description:
        "URL des HTTP-Listeners, die verwendet wird, wenn dieses Berechtigungsprofil den Netzwerkzugriff in der Sandbox aktiviert.",
    },
    {
      key: "permissions.<name>.network.enable_socks5",
      type: "boolean",
      description:
        "Stellt SOCKS5-Unterstützung bereit, wenn dieses Berechtigungsprofil den Netzwerkzugriff in der Sandbox aktiviert.",
    },
    {
      key: "permissions.<name>.network.socks_url",
      type: "string",
      description: "Von diesem Berechtigungsprofil verwendeter SOCKS5-Proxy-Endpunkt.",
    },
    {
      key: "permissions.<name>.network.enable_socks5_udp",
      type: "boolean",
      description: "Erlaubt bei Aktivierung UDP über den SOCKS5-Listener.",
    },
    {
      key: "permissions.<name>.network.allow_upstream_proxy",
      type: "boolean",
      description:
        "Erlaubt, den Netzwerkverkehr aus der Sandbox über einen weiteren Upstream-Proxy zu leiten.",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "Erlaubt Netzwerk-Listenern der Sandbox, sich an Nicht-Loopback-Adressen zu binden. Bei Aktivierung können die Listener auch außerhalb von localhost erreichbar sein.",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "Erlaubt beliebige Unix-Socket-Ziele anstelle der standardmäßig eingeschränkten Zielauswahl. Nur in streng kontrollierten Umgebungen verwenden.",
    },
    {
      key: "permissions.<name>.network.mode",
      type: "limited | full",
      description: "Netzwerkproxy-Modus für den Datenverkehr von Unterprozessen.",
    },
    {
      key: "permissions.<name>.network.domains",
      type: "table",
      description:
        "Domänenregeln für Befehle in der Sandbox. Sie werden nur durchgesetzt, wenn `features.network_proxy` oder aktivierte, von der Administration verwaltete Netzwerkanforderungen den Proxy aktivieren. Unterstützt exakt angegebene Hosts, `*.example.com`, `**.example.com` und globale Zulassungsregeln mit `*`; `deny` hat Vorrang. Schränkt weder die Websuche noch Apps oder MCP-Server ein.",
    },
    {
      key: "permissions.<name>.network.domains.<pattern>",
      type: "allow | deny",
      description:
        "Legt für einen exakt angegebenen Host oder ein Wildcard-Muster mit begrenztem Geltungsbereich wie `*.example.com` oder `**.example.com` fest, ob der Zugriff zugelassen oder verweigert wird.",
    },
    {
      key: "permissions.<name>.network.unix_sockets",
      type: "table",
      description:
        "Überschreibungen für die Unix-Socket-Zulassungsliste beim Netzwerkzugriff in der Sandbox. Verwende Socket-Pfade als Schlüssel; `allow` fügt einen Pfad hinzu, `deny` lehnt ihn ab.",
    },
    {
      key: "permissions.<name>.network.unix_sockets.<path>",
      type: "allow | deny",
      description:
        "Fügt mit `allow` einen absoluten Unix-Socket-Pfad zur effektiven Zulassungsliste hinzu oder lehnt ihn mit `deny` ab. Abgelehnte Einträge werden nicht in die effektive Zulassungsliste aufgenommen.",
    },
    {
      key: "permissions.<name>.network.allow_local_binding",
      type: "boolean",
      description:
        "Erlaubt über den Netzwerkzugriff in der Sandbox einen umfassenderen Zugriff auf lokale oder private Netzwerke. Zulassungsregeln für exakt angegebene lokale IP-Adressen oder `localhost` können auch dann bestimmte lokale Ziele freigeben, wenn diese Einstellung `false` bleibt.",
    },
    {
      key: "projects.<path>.trust_level",
      type: "string",
      description:
        "Kennzeichnet ein Projekt oder einen Worktree als vertrauenswürdig oder nicht vertrauenswürdig (`\"trusted\"` | `\"untrusted\"`). Bei nicht vertrauenswürdigen Projekten werden projektspezifische Ebenen unter `.codex/` übersprungen, darunter projektlokale Konfiguration, Hooks und Regeln.",
    },
    {
      key: "notice.hide_full_access_warning",
      type: "boolean",
      description: "Erfasst, ob der Warnhinweis zum Vollzugriff bestätigt wurde.",
    },
    {
      key: "notice.hide_world_writable_warning",
      type: "boolean",
      description:
        "Erfasst, ob die Warnung zu Windows-Verzeichnissen mit Schreibzugriff für alle bestätigt wurde.",
    },
    {
      key: "notice.hide_rate_limit_model_nudge",
      type: "boolean",
      description: "Erfasst, ob die Erinnerung an einen Modellwechsel aufgrund des Ratenlimits deaktiviert wurde.",
    },
    {
      key: "notice.hide_gpt5_1_migration_prompt",
      type: "boolean",
      description: "Erfasst, ob die Aufforderung zur Migration auf GPT-5.1 bestätigt wurde.",
    },
    {
      key: "notice.hide_gpt-5.1-codex-max_migration_prompt",
      type: "boolean",
      description:
        "Erfasst, ob die Aufforderung zur Migration auf gpt-5.1-codex-max bestätigt wurde.",
    },
    {
      key: "notice.model_migrations",
      type: "map<string,string>",
      description: "Erfasst bestätigte Modellmigrationen als Zuordnungen im Format old->new.",
    },
    {
      key: "forced_login_method",
      type: "chatgpt | api",
      description: "Beschränkt Codex auf eine bestimmte Authentifizierungsmethode.",
    },
    {
      key: "forced_chatgpt_workspace_id",
      type: "string (uuid)",
      description: "Beschränkt ChatGPT-Anmeldungen auf eine bestimmte Workspace-Kennung.",
    },
  ]}
  client:load
/>

Das aktuelle JSON-Schema für `config.toml` findest du [hier](/codex/config-schema.json).

Um beim Bearbeiten von `config.toml` in VS Code oder Cursor Autovervollständigung und Diagnosemeldungen zu erhalten, kannst du die Erweiterung [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) installieren und diese Zeile am Anfang deiner `config.toml` einfügen:

```toml
#:schema https://developers.openai.com/codex/config-schema.json

Hinweis: Benenne `experimental_instructions_file` in `model_instructions_file` um. Codex stuft den alten Schlüssel als veraltet ein. Aktualisiere bestehende Konfigurationen und verwende den neuen Namen.

## `requirements.toml`

`requirements.toml` ist eine von der Administration vorgegebene Konfigurationsdatei, die sicherheitsrelevante Einstellungen verbindlich einschränkt. Nutzende können diese Vorgaben nicht überschreiben. Details, Speicherorte und Beispiele findest du unter [Von der Administration vorgegebene Anforderungen](/de-DE/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

Für Nutzende von ChatGPT Business und ChatGPT Enterprise kann Codex auch aus der Cloud abgerufene
Anforderungen anwenden. Auf der Sicherheitsseite findest du Details dazu, welche Einstellungen Vorrang haben.

Verwende `[features]` in `requirements.toml`, um Feature-Flags für die Laufzeit anhand derselben
kanonischen Schlüssel verbindlich festzulegen, die auch `config.toml` verwendet. Anforderungen können außerdem dokumentierte
Schlüssel enthalten, die nur für die App gelten und nicht in `config.toml` gehören. Nicht angegebene Schlüssel bleiben
uneingeschränkt.

Einige verwaltete Anforderungen erzwingen einen exakten Konfigurationswert statt einer
Zulassungsliste. Nutzende können verbindlich vorgegebene Pfade, Update-Einstellungen,
Login-Shell-Richtlinien, Feedback-Einstellungen oder Einstellungen für den privaten Windows-Desktop nicht überschreiben.

Verwaltete Zulassungslisten für Berechtigungsprofile erfordern Codex 0.138.0 oder höher. Codex
0.137.0 und ältere Versionen ignorieren `allowed_permission_profiles` sowie die verwaltete Einstellung
`default_permissions`.

Verwende `allowed_sandbox_modes` zusammen mit `sandbox_mode`. Verwende für Bereitstellungen mit
Berechtigungsprofilen `allowed_permission_profiles` zusammen mit der verwalteten Einstellung
`default_permissions`.

Die Tabelle `[models.new_thread]` enthält verwaltete Standardwerte, erzwingt sie aber nicht.
Explizite Startoptionen über spezielle CLI-Flags oder Überschreibungen mit `--config` haben
Vorrang. Wird das Modell oder der Reasoning-Aufwand explizit überschrieben, werden beide verwalteten
Modellfelder übersprungen; `service_tier` ist davon unabhängig.

Die Browser-Anforderungen betreffen drei getrennte Bereiche. `in_app_browser`
steuert den Browserbereich, den eine Person selbst öffnet und direkt bedient. `browser_use`
steuert die Arbeit von Agenten im Browser. `computer_use` steuert die Arbeit von Agenten
in nativen Desktop-Apps.

Die verschachtelten Richtlinienwerte für Browser und Computernutzung gewähren für sich allein
keinen Zugriff. Ein origin- oder appspezifisches `allow` kann den Standardwert derselben
Richtlinienquelle überschreiben. Die üblichen Prüfungen von Funktionen, Genehmigungen und weiteren Richtlinien
gelten jedoch weiterhin. Wenn sowohl verwaltete Anforderungen als auch `config.toml` gelten, hat ein `deny`
aus einer der beiden Quellen Vorrang.

<ConfigTable
  options={[
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "Legt verbindlich das Verzeichnis fest, in dem Codex den SQLite-basierten Laufzeitzustand speichert.",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description: "Legt verbindlich das Verzeichnis fest, in das Codex lokale Protokolldateien schreibt.",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description: "Legt verbindlich den JSON-Modellkatalog fest, den Codex beim Start verwendet.",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description: "Legt verbindlich fest, ob Codex beim Start nach Updates sucht.",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description: "Legt verbindlich fest, ob Shell-Tools eine Login-Shell starten dürfen.",
    },
    {
      key: "feedback",
      type: "table",
      description: "Verwaltete Feedback-Einstellungen.",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "Legt verbindlich fest, ob Nutzende über Codex-Clients Feedback senden können.",
    },
    {
      key: "allowed_approval_policies",
      type: "array<string>",
      description:
        "Zulässige Werte für `approval_policy` (zum Beispiel `untrusted`, `on-request`, `never` und `granular`).",
    },
    {
      key: "allowed_approvals_reviewers",
      type: "array<string>",
      description:
        "Zulässige Werte für `approvals_reviewer`, etwa `user` und `auto_review`.",
    },
    {
      key: "guardian_policy_config",
      type: "string",
      description:
        "Verwaltete Richtlinienvorgaben in Markdown für die automatische Überprüfung. Sie haben Vorrang vor der lokalen Einstellung `[auto_review].policy`. Leere Werte werden ignoriert.",
    },
    {
      key: "allowed_permission_profiles",
      type: "table<boolean>",
      description:
        "Vollständige Liste der zulässigen Berechtigungsprofile. Profile mit dem Wert `true` sind zulässig. Profile, die fehlen oder auf `false` gesetzt sind, sind gesperrt. Das gilt auch für Profile, die in künftigen Versionen hinzukommen. Beim Zusammenführen von Anforderungsquellen werden Einträge anhand des Profilnamens zugeordnet.",
    },
    {
      key: "allowed_permission_profiles.<name>",
      type: "boolean",
      description:
        "Erlaubt oder sperrt ein integriertes oder benutzerdefiniertes Berechtigungsprofil, das in einer geladenen Konfiguration oder Anforderungsquelle definiert ist. Eine spätere Anforderungsquelle mit höherer Priorität kann mit `false` ein Profil deaktivieren, das eine frühere Quelle mit niedrigerer Priorität erlaubt.",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "Verwaltetes Standardberechtigungsprofil. Das Profil muss durch `allowed_permission_profiles` zugelassen sein. Lege diesen Wert explizit fest, um ein vorhersehbares Verhalten zu gewährleisten. Fehlt er, verwendet Codex nur dann standardmäßig `:workspace`, wenn sowohl `:workspace` als auch `:read-only` explizit zugelassen sind.",
    },
    {
      key: "enforce_residency",
      type: "string",
      description:
        "Schreibt vor, dass der Datenverkehr des Codex-Dienstes eine unterstützte Datenresidenz verwendet. Derzeit wird `us` akzeptiert.",
    },
    {
      key: "models",
      type: "table",
      description:
        "Verwaltete Modellstandardwerte für neue Threads. Diese Werte haben Vorrang vor Benutzer- und Projektstandardwerten, lassen sich aber durch eine explizite Auswahl für den neuen Thread überschreiben.",
    },
    {
      key: "models.new_thread",
      type: "table",
      description:
        "Standardwerte, die beim Start eines neuen lokalen Threads gelten. Jede Modelleinstellung ist optional.",
    },
    {
      key: "models.new_thread.model",
      type: "string",
      description:
        "Standardmodell für neue Threads. Eine explizite Angabe über `--model` oder eine Überschreibung des Modells oder Reasoning-Aufwands über `--config` hat Vorrang.",
    },
    {
      key: "models.new_thread.model_reasoning_effort",
      type: "string",
      description:
        "Standardmäßiger Reasoning-Aufwand für neue Threads. Wird das Modell oder der Reasoning-Aufwand explizit überschrieben, werden beide verwalteten Modellfelder ignoriert.",
    },
    {
      key: "models.new_thread.service_tier",
      type: "string",
      description:
        "Standardservicestufe für neue Threads. Eine explizite Überschreibung der Servicestufe hat unabhängig von den Modellfeldern Vorrang.",
    },
    {
      key: "permissions",
      type: "table",
      description:
        "Administrativ definierte Berechtigungsprofile mit dem Profilnamen als Schlüssel. Verwendet dieselben Profilfelder wie `config.toml`.",
    },
    {
      key: "permissions.<name>",
      type: "table",
      description:
        "Administrativ definiertes Berechtigungsprofil. Der Name darf weder mit `:` beginnen noch dem reservierten Namen `filesystem` oder dem Namen eines Profils aus einer geladenen Konfiguration entsprechen. Verwendet dieselben Profilfelder wie `config.toml`; das vollständige Profilschema findest du im Leitfaden zu Berechtigungen.",
    },
    {
      key: "allowed_sandbox_modes",
      type: "array<string>",
      description: "Zulässige Werte für `sandbox_mode`.",
    },
    {
      key: "windows",
      type: "table",
      description: "Anforderungen an die native Windows-Sandbox.",
    },
    {
      key: "windows.allowed_sandbox_implementations",
      type: "array<string>",
      description:
        "Zulässige Implementierungen der nativen Windows-Sandbox für `windows.sandbox` (`elevated` und `unelevated`). Die Liste darf nicht leer sein. Wenn beide zulässig sind und kein Modus ausgewählt ist, bevorzugt Codex `elevated`.",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "Legt verbindlich fest, ob die native Windows-Sandbox ihren untergeordneten Prozess auf einem privaten Desktop startet.",
    },
    {
      key: "remote_sandbox_config",
      type: "array<table>",
      description:
        "Hostspezifische Sandbox-Anforderungen. Der erste Eintrag, dessen `hostname_patterns` auf den ermittelten Hostnamen passen, überschreibt `allowed_sandbox_modes` auf oberster Ebene für diese Anforderungsquelle. Hostspezifische Einträge überschreiben derzeit nur Sandbox-Modi.",
    },
    {
      key: "remote_sandbox_config[].hostname_patterns",
      type: "array<string>",
      description:
        "Muster für Hostnamen ohne Unterscheidung zwischen Groß- und Kleinschreibung. Unterstützt `*` für eine beliebige Zeichenfolge und `?` für ein einzelnes Zeichen.",
    },
    {
      key: "remote_sandbox_config[].allowed_sandbox_modes",
      type: "array<string>",
      description:
        "Zulässige Sandbox-Modi, die gelten, wenn dieser hostspezifische Eintrag zutrifft.",
    },
    {
      key: "allowed_web_search_modes",
      type: "array<string>",
      description:
        "Zulässige Werte für `web_search` (`disabled`, `cached`, `indexed`, `live`). `disabled` ist immer zulässig; eine leere Liste lässt praktisch nur `disabled` zu.",
    },
    {
      key: "allow_managed_hooks_only",
      type: "boolean",
      description:
        "Bei `true` überspringt Codex Hooks auf Benutzer-, Projekt- und Sitzungsebene sowie Plug-in-Hooks. Verwaltete Hooks aus `requirements.toml` und anderen verwalteten Konfigurationsebenen bleiben zulässig.",
    },
    {
      key: "allow_appshots",
      type: "boolean",
      description:
        "Setze den Wert auf `false`, um Appshots für verwaltete Nutzerkonten zu deaktivieren. Wird der Wert weggelassen, schränken die Anforderungen Appshots nicht ein. Es gilt dann die reguläre Produktverfügbarkeit.",
    },
    {
      key: "allow_remote_control",
      type: "boolean",
      description:
        "Setze den Wert auf `false`, um die Fernsteuerung von Geräten für verwaltete Nutzerkonten zu deaktivieren. Wird der Wert weggelassen, schränken die Anforderungen die Fernsteuerung von Geräten nicht ein. Es gilt dann die reguläre Produktverfügbarkeit.",
    },
    {
      key: "allow_browser_and_computer_use",
      type: "boolean",
      description:
        "Setze den Wert auf `false`, um sowohl die agentengesteuerte Funktion „Browser“ als auch die Computernutzung in nativen Apps zu blockieren. Der Wert `true` oder das Weglassen des Werts aktiviert keine der beiden Funktionen. Die übrigen Funktions-, Richtlinien- und Genehmigungsprüfungen gelten weiterhin.",
    },
    {
      key: "features.plugin_sharing",
      type: "boolean",
      description:
        "Setze den Wert in der über die Cloud verwalteten `requirements.toml` auf `false`, um das Teilen lokal erstellter Plug-ins im Workspace zu deaktivieren.",
    },
    {
      key: "features",
      type: "table",
      description:
        "Festgeschriebene Werte für Funktionen. Verwende für Laufzeitfunktionen die kanonischen Namen aus `config.toml`; dokumentierte Anforderungsschlüssel, die nur für die App gelten, werden hier ebenfalls unterstützt.",
    },
    {
      key: "features.<name>",
      type: "boolean",
      description:
        "Schreibt vor, dass eine dokumentierte Laufzeit- oder App-Funktion aktiviert oder deaktiviert bleibt.",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "Legt für verwaltete Nutzerkonten verbindlich fest, ob die Apps-Integration verfügbar ist.",
    },
    {
      key: "features.in_app_updates",
      type: "boolean",
      description:
        "Setze den Wert in `requirements.toml` auf `false`, um In-App-Updates zu deaktivieren. Wird diese Anforderung weggelassen, bleiben Updates standardmäßig aktiviert.",
    },
    {
      key: "features.in_app_browser",
      type: "boolean",
      description:
        "Setze den Wert in `requirements.toml` auf `false`, um den integrierten Browserbereich zu deaktivieren, den Nutzende selbst öffnen und direkt steuern.",
    },
    {
      key: "features.browser_use",
      type: "boolean",
      description:
        "Setze den Wert in `requirements.toml` auf `false`, um die agentengesteuerte Funktion „Browser“ zu deaktivieren.",
    },
    {
      key: "features.browser_use_external",
      type: "boolean",
      description:
        "Setze den Wert in `requirements.toml` auf `false`, um zu verhindern, dass Codex unterstützte Browser über die ChatGPT-Browsererweiterung bedient, einschließlich vorhandener Tabs und angemeldeter Sitzungen.",
    },
    {
      key: "features.browser_use_full_cdp_access",
      type: "boolean",
      description:
        "Setze den Wert in `requirements.toml` auf `false`, um den vollständigen Zugriff auf das Chrome DevTools Protocol in der lokalen Laufzeitumgebung einschließlich des Browser-Entwicklermodus zu deaktivieren. Damit verhinderst du auch, dass die ChatGPT-Desktop-App die entsprechende Einstellung aktiviert. Wird der Wert weggelassen, gilt die reguläre Produktverfügbarkeit.",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "Legt für verwaltete Nutzerkonten verbindlich fest, ob die kanonische Funktion `fast_mode` aktiviert oder deaktiviert ist.",
    },
    {
      key: "features.guardian_approval",
      type: "boolean",
      description:
        "Legt für verwaltete Nutzerkonten verbindlich fest, ob Genehmigungen durch Guardian verfügbar sind.",
    },
    {
      key: "features.memories",
      type: "boolean",
      description: "Legt für verwaltete Nutzerkonten verbindlich fest, ob Erinnerungen verfügbar sind.",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description: "Legt für verwaltete Nutzerkonten verbindlich fest, ob Multi-Agent-Funktionen verfügbar sind.",
    },
    {
      key: "features.plugins",
      type: "boolean",
      description: "Legt für verwaltete Nutzerkonten verbindlich fest, ob Plug-ins verfügbar sind.",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description:
        "Legt für verwaltete Nutzerkonten verbindlich fest, ob der Remote-Plug-in-Katalog verfügbar ist.",
    },
    {
      key: "features.computer_use",
      type: "boolean",
      description:
        "Setze den Wert in `requirements.toml` auf `false`, um die Computernutzung, „Aufzeichnen und Wiedergeben“ sowie zugehörige Installations- oder Aktivierungsabläufe zu deaktivieren.",
    },
    {
      key: "features.workspace_dependencies",
      type: "boolean",
      description:
        "Legt für verwaltete Nutzerkonten verbindlich fest, ob die mitgelieferte Laufzeitumgebung für Workspace-Abhängigkeiten verfügbar ist.",
    },
    {
      key: "in_app_browser",
      type: "table",
      description:
        "Anforderungen an den integrierten Browserbereich. Diese Einstellungen steuern nicht die agentengesteuerte Funktion „Browser“.",
    },
    {
      key: "in_app_browser.allow_external_browser_settings_import",
      type: "boolean",
      description:
        "Setze den Wert auf `false`, um zu verhindern, dass Nutzende Einstellungen oder Browserdaten aus einem externen Browser in den integrierten Browser importieren. Bei `true` oder fehlendem Wert bleibt der Import verfügbar, sofern andere Produktprüfungen ihn zulassen. Diese Einstellung lässt sich ausschließlich administrativ verwalten und nicht über `config.toml` überschreiben.",
    },
    {
      key: "browser_use",
      type: "table",
      description: "Verwaltete Anforderungen an die agentengesteuerte Funktion „Browser“.",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "Setze den Wert auf `false`, um zu verhindern, dass die Funktion „Browser“ den Browserverlauf liest. Bei `true` oder fehlendem Wert gelten weiterhin die regulären Verlaufseinstellungen und Verfügbarkeitsprüfungen.",
    },
    {
      key: "browser_use.disable_auto_review",
      type: "boolean",
      description:
        "Setze den Wert auf `true`, um die automatische Überprüfung für die Funktion „Browser“ zu überspringen und stattdessen die nutzende Person um Genehmigung zu bitten. Bei `false` oder fehlendem Wert bleibt die automatische Überprüfung verfügbar, sofern andere Einstellungen sie zulassen.",
    },
    {
      key: "browser_use.allow_global_persistent_approval",
      type: "boolean",
      description:
        "Setze den Wert auf `false`, um zu verhindern, dass die Funktion „Browser“ websiteübergreifende Genehmigungen vom Typ `Always allow` erstellt oder berücksichtigt, etwa für Downloads von beliebigen Websites. Vorhandene gespeicherte Genehmigungen werden ignoriert, aber nicht gelöscht. Der Wert `true` oder das Weglassen des Werts erstellt keine Genehmigung.",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "Rückfallwert für jede Einstellung der Funktion „Browser“, wenn kein passender Eintrag unter `browser_use.origins` sie definiert. Eine passende Origin-Regel ersetzt den Rückfallwert für diese Quelle. Anschließend wendet Codex das strengere Ergebnis aus verwalteten Anforderungen und Benutzerkonfiguration an.",
    },
    {
      key: "browser_use.default_origin_policy.access",
      type: "allow | deny",
      description:
        "Verwende `deny`, um die Funktion „Browser“ für Origins zu blockieren, für die der Rückfallwert gilt. Eine gesperrte Origin blockiert dort auch Uploads, Downloads, den vollständigen Browser-Debugging-Zugriff und die automatische Überprüfung. `allow` lässt lediglich die regulären Genehmigungs- und Richtlinienprüfungen fortfahren.",
    },
    {
      key: "browser_use.default_origin_policy.downloads",
      type: "allow | deny",
      description:
        "Verwende `deny`, um Downloads über die Funktion „Browser“ für Origins zu blockieren, für die der Rückfallwert gilt. `allow` lässt lediglich die regulären Genehmigungs- und Richtlinienprüfungen fortfahren.",
    },
    {
      key: "browser_use.default_origin_policy.uploads",
      type: "allow | deny",
      description:
        "Verwende `deny`, um Uploads über die Funktion „Browser“ für Origins zu blockieren, für die der Rückfallwert gilt. `allow` lässt lediglich die regulären Genehmigungs- und Richtlinienprüfungen fortfahren.",
    },
    {
      key: "browser_use.default_origin_policy.full_cdp_access",
      type: "allow | deny",
      description:
        "Verwende `deny`, um den vollständigen Zugriff auf das Chrome DevTools Protocol (CDP) für Origins zu blockieren, für die der Rückfallwert gilt. `allow` lässt lediglich die regulären Prüfungen der ausdrücklichen Aktivierung und der Genehmigungen fortfahren.",
    },
    {
      key: "browser_use.default_origin_policy.auto_review",
      type: "allow | deny",
      description:
        "Verwende `deny`, um die automatische Überprüfung für Origins zu überspringen, für die der Rückfallwert gilt, und stattdessen die nutzende Person um Genehmigung zu bitten. Mit `allow` bleibt die automatische Überprüfung verfügbar, sofern andere Einstellungen sie zulassen.",
    },
    {
      key: "browser_use.default_origin_policy.persistent_approval",
      type: "boolean",
      description:
        "Setze den Wert auf `false`, um zu verhindern, dass die Funktion „Browser“ eine Genehmigung vom Typ `Always allow` für Origins speichert oder berücksichtigt, für die der Rückfallwert gilt. Genehmigungen für den aktuellen Turn oder Thread können weiterhin gelten. `true` macht `Always allow` verfügbar, sofern es anderweitig zulässig ist, erstellt aber keine Genehmigung.",
    },
    {
      key: "browser_use.default_origin_policy.access_approval_lifetime",
      type: "turn | thread",
      description:
        "Legt fest, wie lange eine nicht dauerhaft gespeicherte Genehmigung für den Websitezugriff gilt: `turn` beschränkt sie auf den aktuellen Turn, `thread` erhält sie für den Rest des aktuellen Threads. `persistent_approval` steuert unabhängig davon, ob `Always allow` verfügbar ist. Der Produktstandard ist `thread`.",
    },
    {
      key: "browser_use.origins",
      type: "map<string, table>",
      description:
        "Origin-spezifische Richtlinien für die Funktion „Browser“. Schlüssel verwenden `<scheme>://<host-pattern>[:<port>]` mit `http` oder `https`. Verwende einen exakt angegebenen Host, `*.example.com` nur für Subdomains oder `**.example.com` für die Basisdomain und ihre Subdomains. Andere `*`-Platzhalter können auch Punkte einschließen, sodass `region*.example.com` auch auf `region.api.example.com` passt. Ein Hostwert von `*` passt auf jeden Host mit diesem Schema. Schemas und vom Standard abweichende Ports sind relevant; explizite Standardports werden bei der Normalisierung entfernt. Pfade, Abfrageparameter, eingebettete Benutzernamen oder Passwörter sowie Platzhalter in Schemas oder Ports sind ungültig. Setze das Muster in TOML in Anführungszeichen, zum Beispiel `[browser_use.origins.\"https://**.example.com\"]`.",
    },
    {
      key: "browser_use.origins.<pattern>",
      type: "table",
      description:
        "Richtlinie für Origins, die auf dieses Muster passen. Passen mehrere Muster, verwendet Codex für jede Funktion den restriktivsten Wert: `deny` vor `allow`, `false` vor `true` und `turn` vor `thread`.",
    },
    {
      key: "browser_use.origins.<pattern>.access",
      type: "allow | deny",
      description:
        "Verwende `deny`, um die Funktion „Browser“ für passende Origins zu blockieren. Die Sperre blockiert dort auch Uploads, Downloads, den vollständigen Browser-Debugging-Zugriff und die automatische Überprüfung. `allow` lässt lediglich die regulären Genehmigungs- und Richtlinienprüfungen fortfahren.",
    },
    {
      key: "browser_use.origins.<pattern>.downloads",
      type: "allow | deny",
      description:
        "Verwende `deny`, um Downloads über die Funktion „Browser“ für passende Origins zu blockieren. `allow` lässt lediglich die regulären Genehmigungs- und Richtlinienprüfungen fortfahren.",
    },
    {
      key: "browser_use.origins.<pattern>.uploads",
      type: "allow | deny",
      description:
        "Verwende `deny`, um Uploads über die Funktion „Browser“ für passende Origins zu blockieren. `allow` lässt lediglich die regulären Genehmigungs- und Richtlinienprüfungen fortfahren.",
    },
    {
      key: "browser_use.origins.<pattern>.full_cdp_access",
      type: "allow | deny",
      description:
        "Verwende `deny`, um den vollständigen Zugriff auf das Chrome DevTools Protocol (CDP) für passende Origins zu blockieren. `allow` lässt lediglich die regulären Prüfungen der ausdrücklichen Aktivierung und der Genehmigungen fortfahren.",
    },
    {
      key: "browser_use.origins.<pattern>.auto_review",
      type: "allow | deny",
      description:
        "Verwende `deny`, um die automatische Überprüfung für passende Origins zu überspringen und stattdessen die nutzende Person um Genehmigung zu bitten. Mit `allow` bleibt die automatische Überprüfung verfügbar, sofern andere Einstellungen sie zulassen.",
    },
    {
      key: "browser_use.origins.<pattern>.persistent_approval",
      type: "boolean",
      description:
        "Setze den Wert auf `false`, um zu verhindern, dass die Funktion „Browser“ eine Genehmigung vom Typ `Always allow` für passende Origins speichert oder berücksichtigt. Genehmigungen für den aktuellen Turn oder Thread können weiterhin gelten. `true` macht `Always allow` verfügbar, sofern es anderweitig zulässig ist, erstellt aber keine Genehmigung.",
    },
    {
      key: "browser_use.origins.<pattern>.access_approval_lifetime",
      type: "turn | thread",
      description:
        "Legt fest, wie lange eine nicht dauerhaft gespeicherte Genehmigung für den Websitezugriff auf passende Origins gilt: `turn` beschränkt sie auf den aktuellen Turn, `thread` erhält sie für den Rest des aktuellen Threads. `persistent_approval` steuert unabhängig davon, ob `Always allow` verfügbar ist.",
    },
    {
      key: "computer_use",
      type: "table",
      description:
        "Verwaltete Anforderungen an agentengesteuertes Arbeiten in nativen Desktop-Apps. Sowohl verwaltete App-Regeln als auch App-Regeln aus `config.toml` werden durchgesetzt. Eine App muss von jeder Richtlinienquelle zugelassen sein.",
    },
    {
      key: "computer_use.allow_locked_computer_use",
      type: "boolean",
      description:
        "Setze den Wert auf `false`, um zu verhindern, dass Nutzende die Nutzung bei gesperrtem Gerät auf einem verwalteten macOS-Gerät aktivieren. Diese Anforderung entfernt die Bedienelemente zur Aktivierung; eine bereits aktivierte Nutzung bei gesperrtem Gerät wird dadurch nicht deaktiviert. Ohne diese Angabe gilt die normale Produktverfügbarkeit.",
    },
    {
      key: "computer_use.allow_persistent_approval",
      type: "boolean",
      description:
        "Setze den Wert auf `false`, um die Option zum sitzungsübergreifenden Speichern von App-Genehmigungen zu entfernen. Genehmigungen für die aktuelle Sitzung bleiben verfügbar. Der Wert `true` oder das Weglassen dieser Angabe erteilt keine Genehmigung für eine App.",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "Standardzugriff für native Apps, auf die keine plattformspezifische Regel zutrifft. `deny` blockiert den Zugriff. `allow` lässt lediglich die üblichen Genehmigungs- und Richtlinienprüfungen zu. Der Produktstandard ist `allow`.",
    },
    {
      key: "computer_use.macos",
      type: "table",
      description: "App-Regeln für die Computernutzung unter macOS.",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description:
        "Ordne exakten macOS-Bundle-IDs `allow` oder `deny` zu. Eine passende Regel ersetzt `computer_use.default_app_access` innerhalb derselben Richtlinienquelle. Eine Ablehnung durch verwaltete Anforderungen oder die Benutzerkonfiguration blockiert den Zugriff weiterhin.",
    },
    {
      key: "computer_use.macos.bundle_ids.<bundle-id>",
      type: "allow | deny",
      description:
        "Verwende `deny`, um die exakte Bundle-ID zu blockieren. `allow` überschreibt nur den Standard dieser Richtlinienquelle. Alle anderen Richtlinienquellen und der normale Genehmigungsablauf müssen die App weiterhin zulassen.",
    },
    {
      key: "computer_use.windows",
      type: "table",
      description:
        "App-Regeln für die Computernutzung mit paketierten und nicht paketierten Windows-Apps.",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "Ordne exakten, registrierten Application User Model IDs (AUMIDs) signierter paketierter Apps `allow` oder `deny` zu. Eine passende Regel ersetzt `computer_use.default_app_access` innerhalb derselben Richtlinienquelle.",
    },
    {
      key: "computer_use.windows.aumids.<aumid>",
      type: "allow | deny",
      description:
        "Verwende `deny`, um die exakte Identität der paketierten App zu blockieren. `allow` überschreibt nur den Standard dieser Richtlinienquelle. Alle anderen Richtlinienquellen und der normale Genehmigungsablauf müssen die App weiterhin zulassen.",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "Regeln für signierte, nicht paketierte ausführbare Windows-Dateien. Die Regeln gleichen den verifizierten Herausgeber und die signierten Versionsinformationen der ausführbaren Datei ab, nicht ihren Pfad oder aktuellen Dateinamen. Eine passende Ablehnung hat Vorrang vor passenden Zulassungen. Für nicht signierte ausführbare Dateien gilt `computer_use.default_app_access`. Ausführbare Dateien, deren signierte Identität nicht eindeutig verifiziert werden kann, werden blockiert.",
    },
    {
      key: "computer_use.windows.exes[].publisher_name",
      type: "string",
      description:
        "Erforderlicher exakter Herausgebername aus dem vertrauenswürdigen Signaturzertifikat der ausführbaren Datei, formatiert als Windows-X.500-Distinguished-Name.",
    },
    {
      key: "computer_use.windows.exes[].product_name",
      type: "string",
      description:
        "Erforderlicher exakter `ProductName` aus den signierten Versionsinformationen der ausführbaren Datei.",
    },
    {
      key: "computer_use.windows.exes[].binary_name",
      type: "string",
      description:
        "Optionaler `OriginalFilename` aus den signierten Versionsinformationen der ausführbaren Datei. Beim Abgleich wird die Groß- und Kleinschreibung ignoriert. Wenn eine passende Regel für Herausgeber und Produkt diesen Wert verlangt, die ausführbare Datei ihn aber nicht bereitstellt, blockiert die Computernutzung die ausführbare Datei.",
    },
    {
      key: "computer_use.windows.exes[].access",
      type: "allow | deny",
      description:
        "Erforderliche Zugriffsentscheidung für passende ausführbare Dateien. `deny` blockiert den Zugriff. `allow` überschreibt nur den Standard dieser Richtlinienquelle. Alle anderen Richtlinienquellen und der normale Genehmigungsablauf müssen die App weiterhin zulassen.",
    },
    {
      key: "experimental_network",
      type: "table",
      description:
        "Administrativ verwaltete Netzwerkanforderungen für lokale Befehle in der Sandbox, die über `requirements.toml` durchgesetzt werden. Wenn diese Anforderungen aktiviert sind, können sie den Netzwerkproxy für Befehle ohne `features.network_proxy` starten. Browser-Tools prüfen verwaltete Netzwerksperren und exklusive Zulassungslisten separat. Diese Anforderungen leiten den Browserverkehr nicht durch den Proxy und steuern weder die Websuche noch Apps, MCP-Server, den Datenverkehr nativer Apps oder den Netzwerkzugriff von Codex Cloud.",
    },
    {
      key: "experimental_network.enabled",
      type: "boolean",
      description:
        "Aktiviere die Anforderungen für den Netzwerkzugriff in der Sandbox. Dies gewährt keinen Netzwerkzugriff, wenn die aktive Sandbox den Netzwerkzugriff für Befehle deaktiviert lässt.",
    },
    {
      key: "experimental_network.http_port",
      type: "integer",
      description:
        "Port des HTTP-Listeners auf der Loopback-Adresse für die Anforderungen unter `[experimental_network]`.",
    },
    {
      key: "experimental_network.socks_port",
      type: "integer",
      description:
        "Port des SOCKS5-Listeners auf der Loopback-Adresse für die Anforderungen unter `[experimental_network]`.",
    },
    {
      key: "experimental_network.allow_upstream_proxy",
      type: "boolean",
      description:
        "Erlaube, dass der Netzwerkverkehr der Sandbox über einen weiteren, in der Umgebung festgelegten Proxy geleitet wird.",
    },
    {
      key: "experimental_network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "Erlaube für die Anforderungen unter `[experimental_network]` Listener-Adressen außerhalb von Loopback. Dadurch können Listener auch außerhalb von localhost erreichbar werden.",
    },
    {
      key: "experimental_network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "Erlaube beliebige Unix-Socket-Ziele, statt den Zugriff auf eine Zulassungsliste zu beschränken. Verwende dies nur in streng kontrollierten Umgebungen.",
    },
    {
      key: "experimental_network.domains",
      type: "map<string, allow | deny>",
      description:
        "Administrative Domainrichtlinie als Schlüssel-Wert-Zuordnung für den Netzwerkzugriff in der Sandbox. Unterstützt exakte Hosts, `*.example.com` nur für Subdomains, `**.example.com` für die Stammdomain samt Subdomains sowie globale Zulassungsregeln mit `*`. Bevorzuge eng gefasste Regeln, da `*` ausgehenden Zugriff auf öffentliche Ziele weitgehend freigibt. Bei Konflikten hat `deny` Vorrang. Kombiniere dies nicht mit `experimental_network.allowed_domains` oder `experimental_network.denied_domains`.",
    },
    {
      key: "experimental_network.allowed_domains",
      type: "array<string>",
      description:
        "Administrative Zulassungsregeln für den Netzwerkzugriff von Befehlen in der Sandbox, solange der verwaltete Netzwerkproxy aktiviert ist. Diese Regeln gelten nicht für die Websuche, Apps oder MCP-Server. Kombiniere dies nicht mit `experimental_network.domains`.",
    },
    {
      key: "experimental_network.denied_domains",
      type: "array<string>",
      description:
        "Administrative Sperrregeln in Listenform für den Netzwerkzugriff in der Sandbox. Kombiniere dies nicht mit `experimental_network.domains`.",
    },
    {
      key: "experimental_network.managed_allowed_domains_only",
      type: "boolean",
      description:
        "Bei `true` gelten nur administrativ verwaltete Zulassungsregeln, solange die Netzwerkanforderungen für die Sandbox aktiv sind. Ergänzungen der Zulassungsliste durch Nutzende werden ignoriert. Auch ohne verwaltete Zulassungsregeln bleiben von Nutzenden hinzugefügte Domain-Zulassungsregeln unwirksam.",
    },
    {
      key: "experimental_network.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "Administrativ verwaltete Unix-Socket-Richtlinie für den Netzwerkzugriff in der Sandbox.",
    },
    {
      key: "experimental_network.allow_local_binding",
      type: "boolean",
      description:
        "Erlaube der Sandbox einen umfassenderen Zugriff auf lokale und private Netzwerke. Zulassungsregeln für exakte lokale IP-Adressen oder `localhost` können weiterhin bestimmte lokale Ziele erlauben, auch wenn dieser Wert `false` bleibt.",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "Administrativ vorgeschriebene, verwaltete Lebenszyklus-Hooks. Erfordert ein Verzeichnis für verwaltete Hooks und verwendet dasselbe Ereignisschema wie inline definierte `[hooks]` in `config.toml`.",
    },
    {
      key: "hooks.managed_dir",
      type: "string (absolute path)",
      description:
        "Verzeichnis mit verwalteten Hook-Skripten unter macOS und Linux. Bevor Codex verwaltete Hooks lädt, prüft es, ob der Pfad absolut ist und das Verzeichnis existiert.",
    },
    {
      key: "hooks.windows_managed_dir",
      type: "string (absolute path)",
      description:
        "Verzeichnis mit verwalteten Hook-Skripten unter Windows. Bevor Codex verwaltete Hooks lädt, prüft es, ob der Pfad absolut ist und das Verzeichnis existiert.",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "Gruppen von Abgleichsregeln für ein Hook-Ereignis wie `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `SessionStart`, `SessionEnd`, `SubagentStart`, `SubagentStop`, `UserPromptSubmit` oder `Stop`.",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "Hook-Handler für eine Gruppe von Abgleichsregeln. Befehls- und MCP-Tool-Hooks werden unterstützt. Prompt- und Agenten-Hook-Handler werden geparst, aber übersprungen.",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "Führe einen Befehls-Hook im Hintergrund aus, ohne den auslösenden Vorgang zu verzögern. Der Standardwert ist `false`; `SessionEnd` wird immer synchron ausgeführt. Siehe [Hooks im Hintergrund ausführen](/codex/hooks#run-hooks-in-the-background).",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "Ungefährer Token-Schwellenwert pro Handler, ab dem zu großer `additionalContext` auf dem Datenträger gespeichert und dem Modell eine kürzere Vorschau gezeigt wird. Der Standardwert ist `2500`; `0` übergibt den vollständigen Kontext direkt an das Modell. Siehe [Große Hook-Ausgaben](/codex/hooks#large-hook-output).",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "Nur für Windows geltende Befehlsüberschreibung für Befehls-Hooks. Der TOML-Alias `command_windows` wird ebenfalls akzeptiert.",
    },
    {
      key: "permissions.filesystem.deny_read",
      type: "array<string>",
      description:
        "Administrativ vorgeschriebene Sperren für Lesezugriffe auf das Dateisystem. Einträge können Pfade oder Glob-Muster sein. Nutzende können sie nicht durch lokale Konfiguration abschwächen.",
    },
    {
      key: "mcp_servers",
      type: "table",
      description:
        "Zulassungsliste der MCP-Server, die aktiviert werden dürfen. Sowohl der Servername (`<id>`) als auch seine Identität müssen übereinstimmen, damit der MCP-Server aktiviert werden kann. Jeder konfigurierte MCP-Server, der nicht in der Zulassungsliste steht oder dessen Identität nicht übereinstimmt, wird deaktiviert.",
    },
    {
      key: "mcp_servers.<id>.identity",
      type: "table",
      description:
        "Identitätsregel für einen einzelnen MCP-Server. Lege entweder `command` (stdio) oder `url` (streamable HTTP) fest.",
    },
    {
      key: "mcp_servers.<id>.identity.command",
      type: "string | table",
      description:
        "Lasse einen stdio-MCP-Server anhand einer exakt übereinstimmenden Befehlszeichenfolge zu oder verwende eine Abgleichstabelle, die eine exakt übereinstimmende ausführbare Datei und Abgleichsregeln für Argumente in festgelegter Reihenfolge vorschreibt. Bei der Zeichenfolgenform werden weder Argumente noch `cwd`, `env` oder `env_vars` geprüft.",
    },
    {
      key: "mcp_servers.<id>.identity.command.executable",
      type: "string",
      description:
        "Ausführbare Datei, mit der der konfigurierte `command` des stdio-Servers exakt übereinstimmen muss.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args",
      type: "array<table>",
      description:
        "Geordnete Abgleichsregeln für die Argumente eines stdio-Servers. Die konfigurierte Argumentliste muss dieselbe Länge haben, und an jeder Position muss der Abgleich erfolgreich sein. Abgleichsregeln für Befehle prüfen weder `cwd` noch `env` oder `env_vars`.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "Abgleichsoperation für diese Argumentposition.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].value",
      type: "string",
      description: "Wert für einen Argumentabgleich mit `exact` oder `prefix`.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].expression",
      type: "string",
      description:
        "Regulärer Ausdruck für einen Argumentabgleich mit `regex`. Der Ausdruck muss gültig sein und den gesamten Argumentwert erfassen.",
    },
    {
      key: "mcp_servers.<id>.identity.url",
      type: "string | table",
      description:
        "Lasse einen MCP-Server mit Streamable HTTP anhand einer exakt übereinstimmenden URL-Zeichenfolge zu oder verwende eine Tabelle für den Wertabgleich mit `exact`, `prefix` oder `regex`.",
    },
    {
      key: "mcp_servers.<id>.identity.url.match",
      type: "exact | prefix | regex",
      description: "Abgleichsoperation für die konfigurierte MCP-Server-URL.",
    },
    {
      key: "mcp_servers.<id>.identity.url.value",
      type: "string",
      description: "Wert für einen URL-Abgleich mit `exact` oder `prefix`.",
    },
    {
      key: "mcp_servers.<id>.identity.url.expression",
      type: "string",
      description:
        "Regulärer Ausdruck für einen URL-Abgleich mit `regex`. Der Ausdruck muss gültig sein und den gesamten URL-Wert erfassen.",
    },
    {
      key: "plugins",
      type: "table",
      description:
        "Plug-in-spezifische Zulassungslisten für MCP-Server mit der Plug-in-ID als Schlüssel. Wenn diese Tabelle vorhanden ist, werden in Plug-ins enthaltene Server ohne passenden Plug-in- und Servereintrag deaktiviert.",
    },
    {
      key: "plugins.<plugin>.mcp_servers",
      type: "table",
      description:
        "Zulassungsliste für MCP-Server, die in einem Plug-in enthalten sind. Die Anforderungen an Plug-in-Server verwenden dieselben Formate für exakte Identitätsangaben und Abgleichsregeln wie die `mcp_servers`-Anforderungen auf oberster Ebene.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity",
      type: "table",
      description:
        "Identitätsregel für einen in einem Plug-in enthaltenen MCP-Server. Lege entweder `command` (stdio) oder `url` (streamable HTTP) fest.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command",
      type: "string | table",
      description:
        "Lasse den stdio-MCP-Server eines Plug-ins anhand einer exakt übereinstimmenden Befehlszeichenfolge zu oder verwende eine Abgleichstabelle, die eine exakt übereinstimmende ausführbare Datei und Abgleichsregeln für Argumente in festgelegter Reihenfolge vorschreibt.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.executable",
      type: "string",
      description:
        "Ausführbare Datei, mit der der konfigurierte Befehl des im Plug-in enthaltenen stdio-Servers exakt übereinstimmen muss.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args",
      type: "array<table>",
      description:
        "Geordnete Abgleichsregeln für die Argumente eines in einem Plug-in enthaltenen stdio-Servers. Die konfigurierte Argumentliste muss dieselbe Länge haben, und an jeder Position muss der Abgleich erfolgreich sein.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "Abgleichsoperation für diese Argumentposition.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].value",
      type: "string",
      description: "Wert für einen Argumentabgleich mit `exact` oder `prefix`.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].expression",
      type: "string",
      description:
        "Regulärer Ausdruck für einen Argumentabgleich mit `regex`. Der Ausdruck muss den gesamten Argumentwert erfassen.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url",
      type: "string | table",
      description:
        "Lasse den MCP-Server eines Plug-ins mit Streamable HTTP anhand einer exakt übereinstimmenden URL-Zeichenfolge zu oder verwende eine Tabelle für den Wertabgleich mit `exact`, `prefix` oder `regex`.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.match",
      type: "exact | prefix | regex",
      description: "Abgleichsoperation für die URL des im Plug-in enthaltenen MCP-Servers.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.value",
      type: "string",
      description: "Wert für einen URL-Abgleich mit `exact` oder `prefix`.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.expression",
      type: "string",
      description:
        "Regulärer Ausdruck für einen URL-Abgleich mit `regex`. Der Ausdruck muss den gesamten URL-Wert erfassen.",
    },
    {
      key: "marketplaces",
      type: "table",
      description:
        "Administrative Anforderungen für Quellen von Plug-in-Marketplaces. Die Regeln gelten, wenn `restrict_to_allowed_sources` auf `true` gesetzt ist.",
    },
    {
      key: "marketplaces.restrict_to_allowed_sources",
      type: "boolean",
      description:
        "Bei `true` müssen von Nutzenden konfigurierte Marketplace-Quellen beim Hinzufügen von Marketplaces, bei der Installation von Plug-ins und bei der Aktualisierung konfigurierter Git-Marketplaces mit `allowed_sources` übereinstimmen. Von Codex verwaltete OpenAI-Marketplaces bleiben zulässig, wenn ihre Quelle und ihr Name den reservierten Werten entsprechen. Bereits von Nutzenden konfigurierte Marketplaces werden dadurch zur Laufzeit nicht gefiltert.",
    },
    {
      key: "marketplaces.allowed_sources",
      type: "table",
      description:
        "Zulässige Marketplace-Quellen mit administrativ festgelegten Regelnamen als Schlüsseln. Regeln mit unterschiedlichen Namen bleiben über die Anforderungsebenen hinweg erhalten. Für Felder unter demselben Namen gilt die übliche Prioritätsreihenfolge der Ebenen.",
    },
    {
      key: "marketplaces.allowed_sources.<name>",
      type: "table",
      description:
        "Eine Regel für eine erlaubte Quelle. Der endgültige `source`-Wert nach dem Zusammenführen der Vorgaben bestimmt, welche gleichrangigen Felder Codex auswertet.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.source",
      type: "git | host_pattern | local",
      description:
        "Abgleichstyp für Marketplace-Quellen. Verwende `git` für ein einzelnes Repository, `host_pattern` für Git-Hosts, die über einen regulären Ausdruck abgeglichen werden, oder `local` für ein einzelnes Verzeichnis.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.url",
      type: "string",
      description:
        "URL des Git-Repositorys, erforderlich bei `source = \"git\"`. Codex normalisiert die konfigurierten und erlaubten URLs und verlangt anschließend eine exakte Übereinstimmung des Repositorys.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.ref",
      type: "string",
      description:
        "Optionale exakte Git-Referenz für eine `git`-Regel. Wird sie weggelassen, erlaubt die Regel jede Referenz für das passende Repository.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.host_pattern",
      type: "string",
      description:
        "Regulärer Ausdruck, erforderlich bei `source = \"host_pattern\"`. Codex gleicht ihn mit dem in Kleinbuchstaben umgewandelten Hostnamen ab, der aus einer Git-Quelle im HTTPS-, SSH- oder SCP-Stil ausgelesen wird. Verwende `^` und `$`, um eine Übereinstimmung mit dem gesamten Hostnamen zu verlangen.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.path",
      type: "string (absolute path)",
      description:
        "Lokales Marketplace-Verzeichnis, erforderlich bei `source = \"local\"`. Codex verlangt einen absoluten Pfad und vergleicht die Pfade nach der Normalisierung.",
    },
    {
      key: "apps",
      type: "table",
      description:
        "Verwaltete App-Vorgaben mit der App-Kennung als Schlüssel. Die Vorgaben können eine App deaktivieren oder das Genehmigungsverhalten für einzelne Tools einschränken.",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "Setze den Wert auf `false`, um eine App zu deaktivieren. Eine Vorgabe zur Deaktivierung bleibt auch beim Zusammenführen mehrerer Vorgabenquellen einschränkend wirksam.",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "Lege den verwalteten Genehmigungsmodus für ein einzelnes App-Tool fest.",
    },
    {
      key: "rules",
      type: "table",
      description:
        "Administrativ erzwungene Befehlsregeln, die mit `.rules`-Dateien zusammengeführt werden. Regeln aus den Vorgaben müssen einschränkend sein.",
    },
    {
      key: "rules.prefix_rules",
      type: "array<table>",
      description:
        "Liste der erzwungenen Präfixregeln. Jede Regel muss `pattern` und `decision` enthalten.",
    },
    {
      key: "rules.prefix_rules[].pattern",
      type: "array<table>",
      description:
        "Befehlspräfix, ausgedrückt als Muster-Token. Jedes Token legt entweder `token` oder `any_of` fest.",
    },
    {
      key: "rules.prefix_rules[].pattern[].token",
      type: "string",
      description: "Ein einzelnes wörtlich abzugleichendes Token an dieser Position.",
    },
    {
      key: "rules.prefix_rules[].pattern[].any_of",
      type: "array<string>",
      description: "Eine Liste erlaubter alternativer Token an dieser Position.",
    },
    {
      key: "rules.prefix_rules[].decision",
      type: "prompt | forbidden",
      description:
        "Erforderlich. Regeln aus den Vorgaben können nur eine Genehmigung anfordern oder etwas verbieten, aber nicht erlauben.",
    },
    {
      key: "rules.prefix_rules[].justification",
      type: "string",
      description:
        "Optionale, nicht leere Begründung, die in Genehmigungsanfragen oder Ablehnungsmeldungen angezeigt wird.",
    },
  ]}
  client:load
/>

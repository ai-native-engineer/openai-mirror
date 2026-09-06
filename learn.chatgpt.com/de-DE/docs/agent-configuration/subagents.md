<!-- source: https://learn.chatgpt.com/de-DE/docs/agent-configuration/subagents -->

ChatGPT Work und Codex können Arbeitsabläufe mit Subagenten ausführen, indem sie spezialisierte Agenten parallel starten und deren Ergebnisse anschließend in einer Antwort zusammenfassen. Das kann besonders bei komplexen Aufgaben helfen, die sich gut parallelisieren lassen, etwa beim Erkunden einer Codebasis oder beim Umsetzen eines mehrstufigen Plans für eine Funktion.

In lokalen Codex-Clients kannst du außerdem benutzerdefinierte Agenten mit unterschiedlichen Modellkonfigurationen und Anweisungen für verschiedene Aufgaben definieren.

## Verfügbarkeit

ChatGPT Work stellt berechtigten Konten Arbeitsabläufe mit Subagenten und eine Anzeige ihrer Aktivitäten zur Verfügung.

<a id="custom-agents"></a>

In aktuellen Codex-Versionen sind Arbeitsabläufe mit Subagenten standardmäßig aktiviert. Die Aktivitäten der Subagenten werden in der ChatGPT-Desktop-App, der Codex CLI und der IDE-Erweiterung angezeigt.

Da jeder Subagent eigene Modell- und Tool-Aufrufe ausführt, verbrauchen Arbeitsabläufe mit Subagenten mehr Token als vergleichbare Ausführungen mit einem einzelnen Agenten.

Weise ChatGPT in ChatGPT Work an, unabhängige Aufgaben an Subagenten zu delegieren. Die Agenten laufen in der von ChatGPT gehosteten Umgebung, und der Chat zeigt ihre Aktivitäten und Ergebnisse an. Fordere die Delegation bei den meisten Intelligenzstufen ausdrücklich an. Mit Ultra kann ChatGPT Arbeit proaktiv delegieren, wenn parallele Agenten die Geschwindigkeit oder Qualität deutlich verbessern würden.

Weise Codex in einem Chat in der App an, unabhängige Teile der Arbeit an
Subagenten zu delegieren. Aktuelle lokale Codex-Versionen delegieren Arbeit, wenn du direkt darum bittest oder wenn
zutreffende Anweisungen in `AGENTS.md` oder Skills dies verlangen. Die App zeigt jeden
Subagenten-Thread an, damit du seine Arbeit und die an den Haupt-Chat zurückgegebene Zusammenfassung
prüfen kannst.

Weise Codex in einer interaktiven CLI-Sitzung an, Subagenten zu verwenden. Codex kann auch
zutreffenden Anweisungen in `AGENTS.md` oder Skills folgen, die eine Delegation verlangen. Verwende
`/agent`, um laufende Agenten-Threads einzusehen und zwischen ihnen zu wechseln. Der Haupt-Thread
fasst die Ergebnisse der Subagenten in seiner abschließenden Antwort zusammen.

Weise Codex in einem IDE-Chat an, unabhängige Teile der Arbeit an Subagenten zu delegieren.
Codex kann auch zutreffenden Anweisungen in `AGENTS.md` oder Skills folgen, die eine
Delegation verlangen. Wenn die Oberfläche für Hintergrundagenten verfügbar ist, erscheinen aktive Subagenten
über dem Editor. Klappe den Bereich auf, um ihren Status zu sehen, alle aktiven
Subagenten anzuhalten oder einen einzelnen Subagenten-Thread zu öffnen.

## Warum Arbeitsabläufe mit Subagenten helfen

Auch mit großen Kontextfenstern haben Modelle Grenzen. Wenn du den Haupt-Chat, in dem du Anforderungen, Einschränkungen und Entscheidungen festlegst, mit unübersichtlichen Zwischenausgaben wie Erkundungsnotizen, Testprotokollen, Stacktraces und Befehlsausgaben überflutest, kann die Sitzung mit der Zeit unzuverlässiger werden.

Dafür werden häufig folgende Begriffe verwendet:

- **Kontextverschmutzung**: Nützliche Informationen gehen in unübersichtlichen Zwischenausgaben unter.
- **Kontextverfall**: Die Leistung lässt nach, wenn sich im Chat weniger relevante Details ansammeln.

Weitere Hintergründe findest du im Chroma-Beitrag über [Kontextverfall](https://research.trychroma.com/context-rot).

Arbeitsabläufe mit Subagenten helfen, indem sie Arbeit mit vielen Zwischenausgaben aus dem Haupt-Thread auslagern:

- Lass den **Hauptagenten** sich auf Anforderungen, Entscheidungen und abschließende Ergebnisse konzentrieren.
- Setze spezialisierte **Subagenten** parallel für Erkundung, Tests oder Protokollanalysen ein.
- Lass Subagenten **Zusammenfassungen** statt unbearbeiteter Zwischenausgaben zurückgeben.

Sie können auch Zeit sparen, wenn sich Aufgaben unabhängig voneinander parallel ausführen lassen. Umfangreichere Aufgaben werden leichter handhabbar, wenn sie in klar abgegrenzte Teilaufgaben zerlegt werden. Codex kann beispielsweise die Analyse eines Dokuments mit mehreren Millionen Token in kleinere Teilprobleme aufteilen und die wichtigsten Erkenntnisse an den Haupt-Thread zurückgeben.

Setze parallele Agenten zunächst für Aufgaben ein, bei denen vor allem gelesen wird, etwa für Erkundung, Tests, Triage und Zusammenfassungen. Gehe bei parallelen Arbeitsabläufen mit vielen Schreibzugriffen vorsichtiger vor: Wenn Agenten gleichzeitig Code bearbeiten, können Konflikte entstehen und der Koordinationsaufwand steigen.

## Grundbegriffe

Codex verwendet bei Arbeitsabläufen mit Subagenten einige verwandte Begriffe:

- **Arbeitsablauf mit Subagenten**: Ein Ablauf, bei dem Codex Agenten parallel ausführt und ihre Ergebnisse zusammenführt.
- **Subagent**: Ein Agent, den Codex startet, um ihm eine bestimmte Aufgabe zu übertragen.
- **Agenten-Thread**: Der Thread, in dem ein Subagent seine Arbeit erledigt. In unterstützten Clients kannst du diese Threads öffnen, um Fortschritt oder Ergebnisse zu prüfen.

## Arbeitsabläufe mit Subagenten starten

Fordere bei den meisten Intelligenzstufen Subagenten oder parallele Arbeit durch Agenten direkt an. Ultra ermöglicht proaktive Delegation, sodass ChatGPT geeignete unabhängige Aufgaben ohne separate Aufforderung delegieren kann.

Fordere Subagenten oder parallele Arbeit durch Agenten direkt an. Codex kann auch delegieren, wenn zutreffende Projekt- oder Skill-Anweisungen dies verlangen.

Zum manuellen Starten verwendest du direkte Anweisungen wie „starte zwei Agenten“, „delegiere diese Arbeit parallel“ oder „setze pro Punkt einen Agenten ein“. Arbeitsabläufe mit Subagenten verbrauchen mehr Token als vergleichbare Ausführungen mit einem einzelnen Agenten, da jeder Subagent eigene Modell- und Tool-Aufrufe ausführt.

Ein guter Subagenten-Prompt sollte erklären, wie die Arbeit aufgeteilt wird, ob Codex vor dem Fortfahren auf alle Agenten warten soll und welche Zusammenfassung oder Ausgabe zurückgegeben werden soll.

```text
Review this branch with parallel subagents. Spawn one subagent for security risks, one for test gaps, and one for maintainability. Wait for all three, then summarize the findings by category with file references.

## Modelle und Reasoning-Aufwand auswählen

Verschiedene Agenten benötigen unterschiedliche Einstellungen für Modell und Reasoning-Aufwand.

Wähle in ChatGPT Work im Editor ein Modell und eine Intelligenzstufe aus.
Je nach ausgewähltem Modell können die verfügbaren Intelligenzstufen **Leicht**, **Mittel**, **Hoch**,
**Sehr hoch** und **Max** umfassen. **Ultra** ist
nur für berechtigte Konten und unterstützte Modelle verfügbar. Diese Stufe nutzt den maximalen
Reasoning-Aufwand und ermöglicht ChatGPT, geeignete Aufgaben proaktiv an Subagenten zu delegieren.

Fordere bei anderen Intelligenzstufen ausdrücklich Subagenten an, wenn du Arbeit parallel delegieren möchtest.

Wenn du für einen Subagenten weder ein Modell noch `model_reasoning_effort` konfigurierst,
übernimmt er das Modell und den Reasoning-Aufwand des übergeordneten Agenten. Wird bei einer expliziten
Startanforderung oder durch eine Standardeinstellung unter `[agents]` ein Modell ausgewählt, ohne dass
ein Reasoning-Aufwand ausdrücklich angegeben oder konfiguriert ist, verwendet der Subagent den
Standardwert dieses Modells für den Reasoning-Aufwand. Um Intelligenz, Geschwindigkeit und Preis auf die jeweilige Aufgabe abzustimmen,
fordere in deinem Prompt ein bestimmtes Modell oder einen bestimmten Reasoning-Aufwand an,
konfiguriere Standardwerte unter `[agents]` in `config.toml` oder lege `model` und
`model_reasoning_effort` direkt in der Datei des benutzerdefinierten Agenten fest.
Verwende beispielsweise <code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code> für schnelle Durchsichten oder eine Konfiguration von <code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code> mit höherem Reasoning-Aufwand für anspruchsvollere Denkaufgaben.

  Beginne bei den meisten Aufgaben in Codex mit{" "}
<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code>. Verwende{" "}
<code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code>, wenn du
  für leichtere Subagentenaufgaben eine schnellere, kostengünstigere Option möchtest.

### Modellauswahl

- **<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code>**: Beginne mit diesem Modell, wenn deine Agenten anspruchsvolle Aufgaben bearbeiten. Seine Stärken liegen bei unklaren, mehrstufigen Aufgaben, die Planung, Tool-Nutzung, Validierung und eine konsequente Umsetzung unter Einbeziehung eines größeren Kontexts erfordern.
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code>**: Verwende dieses Modell für Agenten, bei denen Geschwindigkeit und Effizienz wichtiger sind als eine tiefgehende Analyse, etwa beim Erkunden, beim Durchsehen großer Textmengen, beim Prüfen großer Dateien oder beim Verarbeiten begleitender Dokumente. Es eignet sich gut für parallel arbeitende Agenten, die dem Hauptagenten zusammengefasste Ergebnisse zurückgeben.
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestNanoModel.slug}</code>**: Verwende dieses Modell für schnelle Agenten mit eng begrenztem Aufgabenbereich, die klar definierte, wiederholbare oder in großer Menge anfallende Aufgaben bearbeiten.

### Reasoning-Aufwand (`model_reasoning_effort`)

- **`ultra`**: Verwende diese Stufe für den höchsten Reasoning-Aufwand, wenn das ausgewählte Modell sie
  unterstützt.
- **`max`** und **`xhigh`**: Verwende diese Stufen für besonders anspruchsvolle Denkaufgaben, wenn das
  ausgewählte Modell sie unterstützt.
- **`high`**: Verwende diese Stufe, wenn ein Agent komplexe Logik nachvollziehen, Annahmen prüfen oder Ausnahmefälle durchgehen muss, etwa bei Agenten für Reviews oder Sicherheitsprüfungen.
- **`medium`**: Ein ausgewogener Standardwert für die meisten Agenten.
- **`low`**: Verwende diese Stufe, wenn die Aufgabe unkompliziert ist und Geschwindigkeit am wichtigsten ist.

Ein höherer Reasoning-Aufwand verlängert die Antwortzeit und erhöht den Token-Verbrauch, kann aber bei komplexen Aufgaben die Qualität verbessern. Weitere Informationen findest du unter [Modelle](/de-DE/codex/models), [Grundlagen der Konfiguration](/de-DE/codex/config-file/config-basic) und [Konfigurationsreferenz](/de-DE/codex/config-file/config-reference).

## Orchestrierung und Thread-Steuerung

ChatGPT oder Codex übernimmt die Orchestrierung der Agenten. Dazu gehören das Starten neuer Subagenten, das Weiterleiten weiterer Anweisungen, das Warten auf Ergebnisse und das Schließen von Agenten-Threads.

Wenn viele Agenten laufen, wartet Codex, bis alle angeforderten Ergebnisse vorliegen, und gibt anschließend eine zusammengefasste Antwort zurück.

Bei den meisten Intelligenzstufen startet ChatGPT Agenten nach einer direkten Aufforderung. Mit Ultra kann ChatGPT auch proaktiv delegieren, wenn parallele Arbeit sinnvoll ist.

Aktuelle lokale Codex-Versionen starten Agenten nach einer direkten Aufforderung oder wenn zutreffende Projekt- oder Skill-Anweisungen dies verlangen.

Probiere den folgenden Prompt in deinem Projekt aus, um zu sehen, wie das funktioniert:

```text
I would like to review the following points on the current PR (this branch vs main). Spawn one agent per point, wait for all of them, and summarize the result for each point.
1. Security issue
2. Code quality
3. Bugs
4. Race
5. Test flakiness
6. Maintainability of the code

## Subagenten verwalten

Öffne **Subagenten** und sieh dir ohne Schreibzugriff die Listen **Aktiv** und **Abgeschlossen** an. Wähle einen
abgeschlossenen Subagenten aus, um seine Details und sein Ergebnis zu prüfen. Die Seitenleiste im Web zeigt
die Aktivitäten der Subagenten an. Sie bietet keine Bedienelemente, um einen einzelnen
Subagenten anzuhalten oder zu steuern.

- Öffne über die im Haupt-Thread angezeigte Aktivität einen Subagenten-Thread, um dessen Arbeit zu prüfen.
- Weise Codex direkt an, einen laufenden Subagenten zu steuern, ihn anzuhalten oder abgeschlossene Subagenten-Threads zu schließen.

  

  

- Verwende `/agent` in der CLI, um zwischen aktiven Agenten-Threads zu wechseln und den laufenden Thread zu prüfen.
- Weise Codex direkt an, einen laufenden Subagenten zu steuern, ihn anzuhalten oder abgeschlossene Agenten-Threads zu schließen.

- Wenn der Bereich für Hintergrundagenten verfügbar ist, klappe ihn auf, um den Status zu prüfen, aktive Subagenten anzuhalten oder einen Subagenten-Thread zu öffnen.
- Weise Codex direkt an, einen laufenden Subagenten zu steuern, ihn anzuhalten oder abgeschlossene Subagenten-Threads zu schließen.

## Genehmigungen und Sandbox-Einstellungen

Subagenten übernehmen deine aktuelle Sandbox-Richtlinie.

ChatGPT Work führt Subagenten in seiner gehosteten Umgebung aus und bietet weder eine lokale Codex-Sandbox noch eine Einstellung für den Genehmigungsmodus. Subagenten verwenden die Tools, die dem übergeordneten Chat zur Verfügung stehen. Berechtigungen für Websites und Konnektoren bleiben toolspezifisch.

Subagenten übernehmen den unter dem Editor ausgewählten Berechtigungsmodus. Wähle den Berechtigungsmodus für den übergeordneten Turn aus, bevor du Codex bittest, Arbeit zu delegieren.

In interaktiven CLI-Sitzungen können Genehmigungsanfragen aus inaktiven Agenten-Threads
erscheinen, auch wenn du gerade den Haupt-Thread ansiehst. Das Genehmigungs-Overlay
zeigt die Bezeichnung des Threads an, aus dem die Anfrage stammt. Du kannst `o` drücken, um diesen Thread zu öffnen, bevor
du die Anfrage genehmigst, ablehnst oder beantwortest.

In nicht interaktiven Abläufen oder wenn bei einer Ausführung keine neue Genehmigungsanfrage angezeigt werden kann, schlägt eine Aktion fehl, die eine neue Genehmigung erfordert. Codex gibt den Fehler dann an den übergeordneten Ablauf zurück.

Wenn Codex einen untergeordneten Agenten startet, übernimmt es auch
die zur Laufzeit geänderten Einstellungen des übergeordneten Turns. Dazu gehören die Sandbox- und Genehmigungseinstellungen, die du während
der Sitzung interaktiv festlegst, etwa Änderungen über `/permissions` oder die Verwendung von `--yolo`. Das gilt auch dann, wenn die ausgewählte
Datei für den benutzerdefinierten Agenten andere Standardwerte vorgibt.

Subagenten übernehmen den unter dem Editor ausgewählten Berechtigungsmodus. Wähle den Berechtigungsmodus für den übergeordneten Turn aus, bevor du Codex bittest, Arbeit zu delegieren.

Du kannst auch die Sandbox-Konfiguration einzelner [benutzerdefinierter Agenten](#custom-agents) überschreiben, etwa indem du für einen ausdrücklich festlegst, dass er ohne Schreibzugriff arbeitet.

## Benutzerdefinierte Agenten

Codex enthält folgende integrierte Agenten:

- `default`: universell einsetzbarer Fallback-Agent.
- `worker`: auf die Ausführung ausgerichteter Agent für Implementierungen und Fehlerbehebungen.
- `explorer`: Agent, der die Codebasis vorwiegend lesend erkundet.

Um eigene benutzerdefinierte Agenten zu definieren, füge eigenständige TOML-Dateien unter
`~/.codex/agents/` für persönliche Agenten oder unter `.codex/agents/` für projektbezogene
Agenten hinzu.

Jede Datei definiert einen benutzerdefinierten Agenten. Codex lädt diese Dateien als Konfigurationsebenen für gestartete Sitzungen. Dadurch können benutzerdefinierte Agenten dieselben Einstellungen überschreiben wie eine normale Codex-Sitzungskonfiguration. Das kann aufwendiger wirken als ein spezielles Agentenmanifest. Mit der Weiterentwicklung der Möglichkeiten zum Erstellen und Teilen kann sich auch das Format ändern.

Jede eigenständige Datei für einen benutzerdefinierten Agenten muss Folgendes definieren:

- `name`
- `description`
- `developer_instructions`

Wenn eine Datei für einen benutzerdefinierten Agenten `model` oder `model_reasoning_effort` festlegt, hat der Wert in
der Datei Vorrang. Vor dem Anwenden der Datei ermittelt Codex jede Einstellung
zunächst aus einem beim Start explizit angegebenen Wert, dann aus dem entsprechenden Standardwert unter `[agents]` und schließlich
aus dem Wert des übergeordneten Agenten. Wenn eine explizite Startanforderung oder ein Standardwert unter `[agents]`
ein Modell auswählt und weder die Anforderung noch der Standardwert einen Reasoning-Aufwand vorgibt,
verwendet Codex den standardmäßigen Reasoning-Aufwand dieses Modells. Eine Datei für einen benutzerdefinierten Agenten, die nur `model`
festlegt, behält diesen zuvor ermittelten Aufwand bei. Lege in der Datei zusätzlich `model_reasoning_effort`
fest, wenn das ausgewählte Modell diesen Aufwand nicht unterstützt oder du einen anderen
verwenden möchtest. Andere Sitzungseinstellungen wie `sandbox_mode`, `mcp_servers`
und `skills.config` werden vom übergeordneten Agenten übernommen, wenn sie in der Datei für den benutzerdefinierten Agenten nicht
festgelegt sind.

### Globale Einstellungen

Globale Einstellungen für Subagenten findest du weiterhin unter `[agents]` in deiner [Konfiguration](/de-DE/codex/config-file/config-basic#configuration-precedence).

| Feld                                       | Typ    | Erforderlich | Zweck                                                             |
| ------------------------------------------- | ------- | :------: | ------------------------------------------------------------------- |
| `agents.enabled`                            | Boolescher Wert |    Nein    | Tools für mehrere Agenten aktivieren oder deaktivieren.                                |
| `agents.max_concurrent_threads_per_session` | Zahl  |    Nein    | Anzahl gleichzeitig geöffneter Threads gestarteter Agenten begrenzen; der Haupt-Thread zählt nicht mit. |
| `agents.default_subagent_model`             | Zeichenfolge  |    Nein    | Standardmodell für gestartete Agenten festlegen.                           |
| `agents.default_subagent_reasoning_effort`  | Zeichenfolge  |    Nein    | Standardmäßigen Reasoning-Aufwand für gestartete Agenten festlegen.                |
| `agents.interrupt_message`                  | Boolescher Wert |    Nein    | Eine für das Modell sichtbare Nachricht erfassen, wenn ein Agenten-Turn unterbrochen wird.   |

**Hinweise:**

- Der Standardwert für `agents.enabled` ist `true`. Setze ihn auf `false`, um Tools für mehrere Agenten zu deaktivieren.
- Wenn du `agents.max_concurrent_threads_per_session` nicht festlegst, wählt Codex den Standardwert. Bestehende Konfigurationen können `agents.max_threads` weiterhin als Legacy-Alias verwenden.
- Beim Start explizit angegebene Werte überschreiben `agents.default_subagent_model` und `agents.default_subagent_reasoning_effort`.
- Der Standardwert für `agents.interrupt_message` ist `true`. Setze ihn auf `false`, um die für das Modell sichtbare Nachricht über die Unterbrechung nicht in den Kontext des Agenten aufzunehmen.
- Wenn der Name eines benutzerdefinierten Agenten mit dem eines integrierten Agenten wie `explorer` übereinstimmt, hat dein benutzerdefinierter Agent Vorrang.

### Dateischema für benutzerdefinierte Agenten

| Feld                    | Typ   | Erforderlich | Zweck                                                         |
| ------------------------ | ------ | :------: | --------------------------------------------------------------- |
| `name`                   | Zeichenfolge |   Ja    | Agentenname, den Codex beim Starten dieses Agenten oder bei Verweisen auf ihn verwendet. |
| `description`            | Zeichenfolge |   Ja    | Hinweise für Nutzende dazu, wann Codex diesen Agenten einsetzen soll.     |
| `developer_instructions` | Zeichenfolge |   Ja    | Grundlegende Anweisungen, die das Verhalten des Agenten definieren.             |

In einer Datei für einen benutzerdefinierten Agenten kannst du außerdem weitere unterstützte Schlüssel aus `config.toml` angeben, etwa `model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers` und `skills.config`.

Codex identifiziert den benutzerdefinierten Agenten anhand des Feldes `name`. Am einfachsten ist es,
für die Datei denselben Namen wie für den Agenten zu verwenden. Maßgeblich ist jedoch
das Feld `name`.

### Beispiele für benutzerdefinierte Agenten

Die besten benutzerdefinierten Agenten sind eng spezialisiert und folgen klaren Vorgaben. Gib jedem Agenten eine klar umrissene Aufgabe,
eine passende Auswahl an Tools und Anweisungen, die verhindern, dass er
in angrenzende Aufgabenbereiche abschweift.

#### Beispiel 1: PR-Review

Dieses Muster verteilt das Review auf drei spezialisierte benutzerdefinierte Agenten:

- `pr_explorer` erfasst die Struktur der Codebasis und trägt Belege zusammen.
- `reviewer` sucht nach Risiken in Bezug auf Korrektheit, Sicherheit und Tests.
- `docs_researcher` prüft die Framework- oder API-Dokumentation über einen speziell dafür vorgesehenen MCP-Server.

Projektkonfiguration (`.codex/config.toml`):

```toml
[agents]
max_concurrent_threads_per_session = 8

`.codex/agents/pr-explorer.toml`:

```toml
name = "pr_explorer"
description = "Read-only codebase explorer for gathering evidence before changes are proposed."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Stay in exploration mode.
Trace the real execution path, cite files and symbols, and avoid proposing fixes unless the parent agent asks for them.
Prefer fast search and targeted file reads over broad scans.
"""

`.codex/agents/reviewer.toml`:

```toml
name = "reviewer"
description = "PR reviewer focused on correctness, security, and missing tests."
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "read-only"
developer_instructions = """
Review code like an owner.
Prioritize correctness, security, behavior regressions, and missing test coverage.
Lead with concrete findings, include reproduction steps when possible, and avoid style-only comments unless they hide a real bug.
"""

`.codex/agents/docs-researcher.toml`:

```toml
name = "docs_researcher"
description = "Documentation specialist that uses the docs MCP server to verify APIs and framework behavior."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Use the docs MCP server to confirm APIs, options, and version-specific behavior.
Return concise answers with links or exact references when available.
Do not make code changes.
"""

[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"

Dieses Setup eignet sich gut für Prompts wie:

```text
Review this branch against main. Have pr_explorer map the affected code paths, reviewer find real risks, and docs_researcher verify the framework APIs that the patch relies on.

#### Beispiel 2: Debugging einer Frontend-Integration

Dieses Muster eignet sich für UI-Regressionen, instabile Abläufe im Browser oder Integrationsfehler, die sowohl den Anwendungscode als auch das Produkt im laufenden Betrieb betreffen.

Projektkonfiguration (`.codex/config.toml`):

```toml
[agents]
max_concurrent_threads_per_session = 6

`.codex/agents/code-mapper.toml`:

```toml
name = "code_mapper"
description = "Read-only codebase explorer for locating the relevant frontend and backend code paths."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Map the code that owns the failing UI flow.
Identify entry points, state transitions, and likely files before the worker starts editing.
"""

`.codex/agents/browser-debugger.toml`:

```toml
name = "browser_debugger"
description = "UI debugger that uses browser tooling to reproduce issues and capture evidence."
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "workspace-write"
developer_instructions = """
Reproduce the issue in the browser, capture exact steps, and report what the UI actually does.
Use browser tooling for screenshots, console output, and network evidence.
Do not edit application code.
"""

[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
startup_timeout_sec = 20

`.codex/agents/ui-fixer.toml`:

```toml
name = "ui_fixer"
description = "Implementation-focused agent for small, targeted fixes after the issue is understood."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
developer_instructions = """
Own the fix once the issue is reproduced.
Make the smallest defensible change, keep unrelated files untouched, and validate only the behavior you changed.
"""

[[skills.config]]
path = "/Users/me/.agents/skills/docs-editor/SKILL.md"
enabled = false

Dieses Setup eignet sich gut für Prompts wie:

```text
Investigate why the settings modal fails to save. Have browser_debugger reproduce it, code_mapper trace the responsible code path, and ui_fixer implement the smallest fix once the failure mode is clear.

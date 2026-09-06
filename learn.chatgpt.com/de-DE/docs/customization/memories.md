<!-- source: https://learn.chatgpt.com/de-DE/docs/customization/memories -->

Mit Erinnerungen können ChatGPT und Codex hilfreichen Kontext aus früheren Aufgaben für
künftige Aufgaben weiterverwenden.
ChatGPT im Web nutzt die Erinnerungsfunktion von ChatGPT, während lokale Codex-Clients einen separaten lokalen
Erinnerungsspeicher mit eigenen Steuerelementen verwenden.

Halte verbindliche Teamvorgaben in `AGENTS.md` oder in eingecheckter Dokumentation fest. Nutze
Erinnerungen als hilfreiche Gedächtnisstütze, aber nicht als einzige Quelle für Regeln, die
immer gelten müssen.

In der ChatGPT-Desktop-App kannst du mit `/memories` festlegen, ob ein Chat
lokale Erinnerungen nutzen oder zur Erstellung künftiger Erinnerungen beitragen darf. Unter
**Einstellungen \> Personalisierung** kannst du die Funktion bei Bedarf ein- oder ausschalten.

Verwalte die Erinnerungsfunktion von ChatGPT unter **Einstellungen \> Personalisierung**. ChatGPT Work verwendet
die für dein Konto und deinen Workspace verfügbaren Erinnerungseinstellungen. Es verwendet weder einen
lokalen Codex-Erinnerungsspeicher noch lokale Steuerelemente für Erinnerungen.

In Codex CLI kannst du in einer interaktiven Sitzung mit `/memories` festlegen, ob der
aktuelle Chat vorhandene lokale Erinnerungen nutzen oder als Eingabe für künftige
Erinnerungen dienen darf. Unter [Lokale Erinnerungen konfigurieren](#configure-local-memories) erfährst du, was zu tun ist, wenn der
Befehl nicht verfügbar ist.

Die IDE-Erweiterung verwendet den lokalen Erinnerungsspeicher des verbundenen Codex-Hosts. Wenn
Erinnerungen für diesen Host aktiviert sind, verwende dieselben Steuerelemente auf Chat-Ebene wie
in Codex CLI.

[Verlauf der Computernutzung](/de-DE/codex/customization/computer-history) ist eine Desktop-Funktion für macOS,
die aus Aktivitäten in zugelassenen Apps und auf zugelassenen Websites Erinnerungen und
eine Zeitleiste erstellt, auf die ChatGPT und Codex zugreifen können.

<a id="how-memories-work"></a>
<a id="memory-storage"></a>
<a id="control-memories-per-thread"></a>
<a id="control-memories-per-chat"></a>
<a id="control-memories-per-task"></a>
<a id="review-memories"></a>

## So funktionieren lokale Codex-Erinnerungen

Nachdem du Erinnerungen aktiviert hast, kann Codex hilfreichen Kontext aus geeigneten früheren
Chats in lokalen Erinnerungsdateien erfassen. Codex überspringt aktive oder nur kurze Sitzungen,
entfernt Secrets aus generierten Erinnerungsfeldern und aktualisiert Erinnerungen
im Hintergrund statt sofort nach dem Ende jedes Chats.

Erinnerungen werden nach dem Ende eines Chats möglicherweise nicht sofort aktualisiert. Codex wartet, bis ein
Chat lange genug inaktiv ist, um zu vermeiden, dass noch laufende Arbeit
zusammengefasst wird.

Bei der Generierung von Erinnerungen kann ein Hintergrunddurchlauf auch übersprungen werden, wenn der verbleibende
Anteil deines Codex-Ratenlimits unter dem konfigurierten Schwellenwert liegt. So verbraucht Codex
kein Kontingent, wenn du kurz vor einem Limit stehst.

## Speicherung lokaler Erinnerungen

Codex speichert Erinnerungen in deinem Codex-Home-Verzeichnis. Standardmäßig ist das
`~/.codex`. Unter [Speicherorte für Konfigurations- und Statusdaten](/de-DE/codex/config-file/config-advanced#config-and-state-locations)
erfährst du, wie Codex `CODEX_HOME` verwendet.

Die wichtigsten Erinnerungsdateien befinden sich unter `~/.codex/memories/`. Sie enthalten Zusammenfassungen,
dauerhafte Einträge, jüngste Eingaben und zugehörige Belege aus früheren Chats.

Betrachte diese Dateien als generierte Statusdaten. Du kannst sie zur Fehlerbehebung
oder vor der Weitergabe deines Codex-Home-Verzeichnisses prüfen. Nutze manuelle Änderungen
jedoch nicht als primäre Steuerungsmöglichkeit.

<a id="control-local-memories-per-task"></a>

## Lokale Erinnerungen pro Chat steuern

In der ChatGPT-Desktop-App und in Codex TUI kannst du mit `/memories` die Erinnerungsfunktion für
den aktuellen Chat steuern. Mit den Optionen auf Chat-Ebene legst du fest, ob der aktuelle
Chat vorhandene Erinnerungen nutzen darf und ob Codex den Chat zum
Generieren künftiger Erinnerungen verwenden darf.

Optionen auf Chat-Ebene ändern deine globalen Erinnerungseinstellungen nicht.

## Lokale Erinnerungen überprüfen

Speichere keine Secrets in Erinnerungen. Codex entfernt Secrets aus generierten
Erinnerungsfeldern. Prüfe die Erinnerungsdateien trotzdem, bevor du dein
Codex-Home-Verzeichnis oder generierte Erinnerungsartefakte weitergibst.

<a id="enable-memories"></a>
<a id="configuration"></a>

## Lokale Erinnerungen konfigurieren

Lokale Codex-Erinnerungen sind standardmäßig deaktiviert. Öffne in der ChatGPT-Desktop-App
**Einstellungen \> Personalisierung** und schalte **Erinnerungen aktivieren** ein.

Füge für die Einrichtung über die Konfiguration das Feature-Flag in `config.toml` ein:

```toml
[features]
memories = true

Die Speicherorte der Konfigurationsdateien und die vollständige Liste der Einstellungen für Erinnerungen findest du unter
[Grundlagen der Konfiguration](/de-DE/codex/config-file/config-basic) sowie in der [Referenz zur
Konfiguration](/de-DE/codex/config-file/config-reference).

Gängige Einstellungen für Erinnerungen sind:

- `memories.generate_memories`: legt fest, ob neu erstellte Chats als
  Eingaben zum Generieren von Erinnerungen gespeichert werden können.
- `memories.use_memories`: legt fest, ob Codex vorhandene Erinnerungen in
  künftige Sitzungen einbindet.
- `memories.disable_on_external_context`: legt mit dem Wert `true` fest, dass Chats, die
  externen Kontext wie MCP-Tool-Aufrufe, Websuche oder Toolsuche verwendet haben, nicht für die
  Generierung von Erinnerungen genutzt werden. Der ältere Schlüssel `memories.no_memories_if_mcp_or_web_search`
  wird weiterhin als Alias akzeptiert.
- `memories.min_rate_limit_remaining_percent`: legt fest, wie viel Prozent des
  Codex-Ratenlimits mindestens verbleiben müssen, bevor die Generierung von Erinnerungen beginnt.
- `memories.extract_model`: überschreibt die Modellauswahl für die Extraktion von Erinnerungen
  aus einzelnen Chats.
- `memories.consolidation_model`: überschreibt die Modellauswahl für die globale Konsolidierung
  von Erinnerungen.

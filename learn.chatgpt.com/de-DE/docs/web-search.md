<!-- source: https://learn.chatgpt.com/de-DE/docs/web-search -->

ChatGPT verfügt über ein eigenes Tool für die Websuche. Behandle alle Suchergebnisse aus dem Web als
nicht vertrauenswürdige Eingaben.

Frage in der ChatGPT-Desktop-App in einem Chat nach aktuellen Informationen. ChatGPT protokolliert
die Suchaktivität zusammen mit den anderen Tool-Aufrufen im Transkript.

Frage in ChatGPT im Web nach aktuellen Informationen oder Quellen. Suchergebnisse und
Quellenangaben erscheinen im Chat, wenn ChatGPT die Websuche verwendet. Die Workspace-Einstellungen
können die Verfügbarkeit der Websuche einschränken.

Rufe die CLI mit `--search` auf, um für einen Durchlauf Live-Ergebnisse abzurufen:

```bash
codex --search "Summarize the latest release notes for this dependency"

Suchvorgänge erscheinen als Einträge des Typs `web_search` im interaktiven Transkript sowie in der von
`codex exec --json` erzeugten Ausgabe.

Fordere Codex in der IDE-Erweiterung auf, während deiner Arbeit im Editor zu suchen. Die
Erweiterung verwendet den Suchmodus des verbundenen Codex-Hosts. Die Suchaktivität erscheint
im Chat-Transkript.

## Lokale Websuche konfigurieren

Für lokale Codex-Chats aktiviert Codex standardmäßig die Suche mit zwischengespeicherten Ergebnissen. Dieser Modus verwendet
einen von OpenAI gepflegten Index, anstatt beliebige Seiten live abzurufen. Das
verringert das Risiko von Prompt Injection, beseitigt es aber nicht.

Die Websuche ist ein gehostetes Tool und vom Netzwerkzugriff lokaler Befehle in der Sandbox getrennt.
Sie verwendet weder den Netzwerkproxy noch die Domain-Zulassungsliste des Berechtigungsprofils und
kann verfügbar bleiben, wenn der Netzwerkzugriff für Befehle deaktiviert ist. Konfiguriere
die Suche nach Bedarf mit `web_search`, `tools.web_search.allowed_domains` und der verwalteten Einstellung
`allowed_web_search_modes`. Filter für Suchdomains schränken
weder den Netzwerkverkehr lokaler Befehle noch Apps, Konnektoren oder MCP-Server ein.

Verwende die Live-Suche, wenn du für deine Aufgabe die neuesten Informationen brauchst. Trage
`web_search = "live"` in `config.toml` ein. Trage `web_search = "disabled"` ein, um
das Tool zu deaktivieren. Der Modus `"indexed"` erlaubt externen Webzugriff nur, wenn der
Suchindex die Anfrage freigibt. Wenn Codex mit Vollzugriff ausgeführt wird, nutzt die Websuche
standardmäßig Live-Ergebnisse. Unter [Grundlagen der Konfiguration](/de-DE/codex/config-file/config-basic)
erfährst du, wo Konfigurationsdateien zu finden sind und welche Prioritätsregeln gelten.

### Mit einem benutzerdefinierten Modellanbieter suchen

Ein benutzerdefinierter Modellanbieter kann für die eigenständige Websuche konfiguriert werden, wenn er
einen kompatiblen Suchendpunkt unterstützt:

```toml
model_provider = "custom"
web_search = "live"

[model_providers.custom]
name = "Custom Responses provider"
base_url = "https://example.com/v1"
env_key = "CUSTOM_RESPONSES_API_KEY"
supports_standalone_web_search = true

Bei benutzerdefinierten Anbietern ist standardmäßig `supports_standalone_web_search = false` festgelegt.
Die eigenständige Websuche wird noch entwickelt und ist standardmäßig deaktiviert.
Das Festlegen dieser Anbieterfunktion allein reicht nicht aus, um die eigenständige Websuche zu aktivieren: Der Anbieter,
das ausgewählte Modell und die Laufzeitumgebung müssen die eigenständige Suche ebenfalls unterstützen. Workspace-Einschränkungen und
verwaltete Suchbeschränkungen gelten weiterhin.

Informationen zu den Netzwerkgrenzen für Codex-Cloud-Umgebungen findest du unter [Zugriff auf das
Internet](/de-DE/codex/cloud/internet-access).

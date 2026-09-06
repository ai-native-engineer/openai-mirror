<!-- source: https://learn.chatgpt.com/de-DE/docs/import -->

Nutze die Importfunktion, um Anweisungen, Einstellungen, Skills, Plug-ins, Projekte
und zuletzt bearbeitete Inhalte eines anderen Agenten in die ChatGPT-Desktop-App oder Codex CLI zu übernehmen.
Die Desktop-App unterstützt Importe aus **Claude Code**, <strong>Claude Cowork</strong>
oder **Cursor**. Codex CLI kann aus **Claude Code** oder **Cursor** importieren.

Die Desktop-App importiert unterstützte Elemente direkt und ermöglicht dir, das Setup für
importierte Plug-ins oder Verbindungen abzuschließen, für die eine Autorisierung erforderlich ist. Außerdem kannst du
importierte Inhalte mit automatischen Updates synchron halten.

Der Import ändert oder löscht dein bestehendes Agenten-Setup nicht.

  

## Import starten

### In der Desktop-App importieren

1. Öffne in der ChatGPT-Desktop-App **Einstellungen \> Import**. Wenn **Import** noch nicht
   als Bereich in den Einstellungen verfügbar ist, öffne **Allgemein** und suche nach **Setup eines anderen
   Agenten importieren**.
2. Wähle **Importieren**.
3. Wähle die Agenten aus, deren Inhalte du übernehmen möchtest, und anschließend **Weiter**.
4. Lege unter **Zu importierende Elemente auswählen** fest, was du übernehmen möchtest, und wähle anschließend **Weiter**.
5. Öffne nach Abschluss des Imports ein importiertes Projekt oder einen importierten Chat, um weiterzuarbeiten.

### Importierte Inhalte synchron halten

Öffne in der ChatGPT-Desktop-App **Einstellungen \> Import** und aktiviere automatische
Updates, damit importierte Inhalte mit dem ursprünglichen Agenten synchron bleiben. Im selben Einstellungsbereich kannst du außerdem
deinen Importverlauf einsehen.

### In Codex CLI importieren

1. Starte eine lokale Codex CLI-Sitzung und gib `/import` ein.
2. Wähle **Claude Code** oder **Cursor**.
3. Wähle das unterstützte Setup, die Projektdateien und die kürzlich geführten Chats aus, die du
importieren möchtest.
4. Prüfe die importierte Konfiguration und arbeite in Codex weiter.

Codex CLI importiert bis zu 50 Chats aus den letzten 30 Tagen. Der Befehl `/import`
ist während einer laufenden Aufgabe, in einer Remote-Sitzung oder bei einer Verbindung
zu einem lokalen App-Server-Daemon nicht verfügbar. Weitere Informationen findest du unter [Slash-Befehle für die
CLI](/codex/developer-commands?surface=cli#cli-import-claude-code-or-cursor-setup-with-import).

  

## So funktioniert der Import

Beim Import werden sowohl dein Setup auf Benutzerebene als auch deine bestehenden Projekte geprüft.
Das Setup auf Benutzerebene basiert auf Dateien auf deinem Computer. Das Setup auf Projektebene basiert
auf Dateien in den von dir ausgewählten Repositories und Ordnern.

Beim Import führt ChatGPT folgende Schritte aus:

1. Erkennt unterstützte Setup-Elemente und zuletzt bearbeitete Inhalte.
2. Importiert die von dir ausgewählten Elemente.
3. Belässt dein bestehendes Agenten-Setup unverändert.
4. Prüft, ob importierte Plug-ins oder Verbindungen noch eingerichtet werden müssen.
5. Zeigt eine Statuskarte an, wenn du das Setup noch abschließen musst.

## Was ChatGPT importieren kann

| Importiertes Element                     | Ziel                                             |
| --------------------------------- | ------------------------------------------------------- |
| Anweisungsdateien                 | [`AGENTS.md`](/de-DE/codex/agent-configuration/agents-md)     |
| `settings.json`                   | [`config.toml`](/de-DE/codex/config-file/config-basic)        |
| Skills                            | [Skills](/de-DE/codex/build-skills)                           |
| Plug-ins                           | Plug-ins                                                 |
| Vorhandene Projektordner          | Projekte, die dieselben Ordner verwenden                         |
| Projekterinnerungen aus Claude Code | [Erinnerungen](/de-DE/codex/customization/memories)               |
| Chats aus den letzten 30 Tagen       | ChatGPT-Chats                                           |
| MCP-Server-Konfiguration          | [Codex-MCP-Konfiguration](/de-DE/codex/extend/mcp)            |
| Hooks                             | [Codex-Hooks](/de-DE/codex/hooks)                             |
| Slash-Befehle                    | [Skills](/de-DE/codex/build-skills)                           |
| Subagenten                         | [Codex-Subagenten](/de-DE/codex/agent-configuration/subagents) |

## Setup nach dem Import abschließen

Nach Abschluss des Imports zeigt die App unten links eine Statuskarte an.
Wenn ein importiertes Plug-in oder eine importierte Verbindung noch eingerichtet werden muss, weist die Karte darauf hin.

Wenn die App auf ein Element hinweist, das weitere Schritte erfordert, wähle **Fertigstellen** und folge den
Anweisungen, um das Setup abzuschließen.

## Was du nach dem Import prüfen solltest

Prüfe das importierte Setup, bevor du dich darauf verlässt. Achte besonders auf:

- Einschränkungen oder Berechtigungen für Tools in importierten Skills und Agenten.
- MCP-Server-Einstellungen, die benutzerdefinierte Authentifizierung, Header, Umgebungsvariablen
oder Transportarten verwenden. Möglicherweise musst du dich erneut anmelden.
- Hooks, die sich nach dem Import möglicherweise anders verhalten.
- Plug-ins, Marketplaces oder andere Setup-Elemente, bei denen weitere manuelle Schritte erforderlich sind.
- Prompt-Vorlagen oder Prompts im Befehlsstil, die von Argumenten,
Shell-Interpolation oder Platzhaltern für Dateipfade abhängen.

## Nach dem Import

Öffne nach Abschluss des Imports eines deiner importierten Projekte und arbeite
dort weiter. Unter [ChatGPT verwenden](/de-DE/codex/use-chatgpt) erfährst du, wie du deine
nächste Aufgabe startest.

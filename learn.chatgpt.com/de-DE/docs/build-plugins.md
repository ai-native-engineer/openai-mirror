<!-- source: https://learn.chatgpt.com/de-DE/docs/build-plugins -->

Nutze zum Erstellen oder Einreichen eines Plug-ins die vollständige
[Entwicklungsdokumentation auf developers.openai.com](/plugins).

<div className="not-prose my-6">
  
    Plug-in erstellen und einreichen
  
</div>

Diese Seite bietet eine kurze Einführung. Ein Plug-in ist ein installierbares Paket,
das Skills, einen MCP-Server oder beides enthalten kann. Ein MCP-Server kann außerdem
optional eine Benutzeroberfläche zurückgeben.

ChatGPT und Codex nutzen dasselbe universelle Plug-in-Verzeichnis. Du brauchst ein öffentliches Plug-in
nur einmal zu veröffentlichen, damit derselbe Eintrag über die unterstützten Oberflächen beider Produkte
auffindbar ist. Nutze während der Entwicklung einen lokalen Marketplace, um das Paket zu testen,
bevor du es für das universelle Verzeichnis einreichst.

Informationen zur Verteilung in einem Workspace über GitHub findest du unter
[Plug-in-Verwaltung](/de-DE/codex/enterprise/plugin-management).

Beginne mit einem Skill, solange du einen persönlichen Ablauf noch weiterentwickelst.
Erstelle ein Plug-in, wenn du diesen Ablauf teilen, zusammengehörige Skills bündeln,
einen externen Dienst anbinden oder für ein Team eine stabile Funktion bereitstellen möchtest.

## Plug-in mit `@plugin-creator` erstellen

Am schnellsten gelingt das Setup mit dem integrierten Skill `@plugin-creator`
im ChatGPT Work-Modus oder mit `$plugin-creator` in Codex.

  
    
  

Beschreibe das gewünschte Ergebnis. Gib an, welche Skills oder welchen MCP-Server das Plug-in enthalten soll
und ob du zum Testen einen Eintrag in einem lokalen Marketplace möchtest. Zum Beispiel:

```text
@plugin-creator Create a plugin named meeting-follow-up.
Include a skill that turns meeting notes into decisions, owners, and next steps.
Add it to a personal marketplace so I can test it locally.

Der Skill erstellt das erforderliche Manifest `.codex-plugin/plugin.json`, strukturiert
den Plug-in-Ordner und kann das Plug-in einem lokalen Marketplace hinzufügen.

  
    
  

Wenn der Skill fertig ist:

1. Überprüfe `.codex-plugin/plugin.json`.
2. Prüfe jeden mitgelieferten Skill unter `skills/`.
3. Lade ChatGPT oder Codex neu und installiere das Plug-in über die zugehörige Quelle
im lokalen Marketplace.
4. Teste das Plug-in in einer neuen Unterhaltung mit typischen Anfragen.

Wenn das Plug-in einen MCP-Server enthält, erstelle und teste zuerst den Server und
übergib `@plugin-creator` anschließend die Daten der registrierten Verbindung. Befolge den vollständigen
[Ablauf für MCP-Server](https://developers.openai.com/plugins/build/mcp-server), der
Tools, Authentifizierung, Bereitstellung und Testing abdeckt.

## Ein Plug-in, das nur Skills enthält, manuell erstellen

Ein minimales Plug-in enthält ein Manifest und mindestens einen Skill:

```text
meeting-follow-up/
├── .codex-plugin/
│   └── plugin.json
└── skills/
    └── meeting-follow-up/
        └── SKILL.md

Erstelle `.codex-plugin/plugin.json`:

```json
{
  "name": "meeting-follow-up",
  "version": "1.0.0",
  "description": "Turn meeting notes into decisions and next steps",
  "skills": "./skills/"
}

Füge anschließend `skills/meeting-follow-up/SKILL.md` hinzu:

```md
---
name: meeting-follow-up
description: Extract decisions, owners, and next steps from meeting notes.
---

Review the meeting notes. Return:

1. Decisions
2. Action items with owners
3. Open questions

Verwende einen stabilen Plug-in-Namen in Kebab-Case. Formuliere die Beschreibung des Skills so konkret,
dass ChatGPT und Codex erkennen, wann der Ablauf zum Einsatz kommt.

Füge den Ordner mit `@plugin-creator` einem lokalen Marketplace hinzu. Installiere und
teste das Plug-in, bevor du es weitergibst.

## Weiter mit der Entwicklungsdokumentation

Die vollständige Entwicklungsdokumentation findest du in der
[Dokumentation zu Plug-ins](https://developers.openai.com/plugins/). Sie behandelt:

- [Plug-in-Architektur](https://developers.openai.com/plugins/concepts/plugins)
- [Skills erstellen](https://developers.openai.com/plugins/build/skills)
- [MCP-Server erstellen](https://developers.openai.com/plugins/build/mcp-server)
- [Optionale Benutzeroberfläche hinzufügen](https://developers.openai.com/plugins/build/chatgpt-ui)
- [Plug-in paketieren](https://developers.openai.com/plugins/build/plugins)
- [Plug-in testen](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [Einreichen und veröffentlichen](https://developers.openai.com/plugins/deploy/submission)

Wie du Plug-ins durchsuchst, installierst, aktivierst oder entfernst, erfährst du unter [Plug-ins
verwenden](/de-DE/codex/plugins).

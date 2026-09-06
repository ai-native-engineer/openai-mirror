<!-- source: https://learn.chatgpt.com/de-DE/docs/customization/overview -->

Mit Anpassungen sorgst du dafür, dass Codex so arbeitet wie dein Team.

In Codex setzt sich die Anpassung aus mehreren Ebenen zusammen, die ineinandergreifen:

- **Projektanweisungen (`AGENTS.md`)** für dauerhafte Vorgaben
- **[Erinnerungen](/de-DE/codex/customization/memories)** für hilfreichen Kontext aus früheren Aufgaben
- **Skills** für wiederverwendbare Arbeitsabläufe und Fachwissen
- **[MCP](/de-DE/codex/extend/mcp)** für den Zugriff auf externe Tools und gemeinsam genutzte Systeme
- **[Subagenten](/de-DE/codex/agent-configuration/subagents)**, um Aufgaben an spezialisierte Subagenten zu delegieren

Diese Ebenen ergänzen einander, statt miteinander zu konkurrieren. `AGENTS.md` gibt das Verhalten vor, Erinnerungen
bewahren lokalen Kontext für spätere Aufgaben, Skills bündeln wiederholbare Prozesse und
[MCP](/de-DE/codex/extend/mcp) verbindet Codex mit Systemen außerhalb des lokalen Workspaces.

## AGENTS-Anweisungen

Mit `AGENTS.md` erhält Codex dauerhafte Projektanweisungen, die mit deinem Repository weitergegeben werden und schon gelten, bevor der Agent seine Arbeit beginnt. Halte die Datei kompakt.

Verwende sie für Regeln, die Codex in einem Repository immer befolgen soll, zum Beispiel:

- Build- und Testbefehle
- Vorgaben für Reviews
- Repository-spezifische Konventionen
- Verzeichnisspezifische Anweisungen

Wenn der Agent falsche Annahmen über deine Codebasis trifft, korrigiere sie in `AGENTS.md` und fordere den Agenten auf, `AGENTS.md` zu aktualisieren, damit die Korrektur dauerhaft gilt. Nutze dies als Feedbackschleife.

**`AGENTS.md` aktualisieren:** Beginne nur mit den wirklich wichtigen Anweisungen. Wandle wiederkehrendes Review-Feedback in Regeln um, speichere Anweisungen im nächstgelegenen Verzeichnis, für das sie gelten, und fordere den Agenten nach einer Korrektur auf, `AGENTS.md` zu aktualisieren. So wird die Korrektur in künftigen Sitzungen übernommen.

### Wann du `AGENTS.md` aktualisieren solltest

- **Wiederkehrende Fehler**: Macht der Agent immer wieder denselben Fehler, füge eine Regel hinzu.
- **Zu hoher Leseaufwand**: Wenn der Agent die richtigen Dateien findet, aber zu viele Dokumente liest, ergänze Routing-Hinweise (welche Verzeichnisse/Dateien priorisiert werden sollen).
- **Wiederkehrendes PR-Feedback**: Wenn du dasselbe Feedback mehr als einmal gibst, halte es als Regel fest.
- **In GitHub**: Markiere in einem Kommentar zu einem Pull Request `@codex` und füge eine Aufforderung hinzu (zum Beispiel `@codex add this to AGENTS.md`), um die Aktualisierung an einen Cloud-Chat zu delegieren.
- **Abweichungsprüfungen automatisieren**: Verwende [geplante Aufgaben](/de-DE/codex/automations), um wiederkehrende Prüfungen (zum Beispiel täglich) auszuführen, die Lücken in den Anweisungen erkennen und Ergänzungen für `AGENTS.md` vorschlagen.

Ergänze `AGENTS.md` um eine Infrastruktur, die diese Regeln durchsetzt: Pre-Commit-Hooks, Linter und Typechecker erkennen Probleme, bevor sie dir auffallen. So verhindert das System wiederkehrende Fehler immer besser.

Codex kann Anweisungen aus mehreren Speicherorten laden: aus einer globalen Datei in deinem Codex-Home-Verzeichnis (für deine persönliche Entwicklungsarbeit) und aus Repository-spezifischen Dateien, die Teams einchecken können. Dateien, die näher am Arbeitsverzeichnis liegen, haben Vorrang.
Lege mit der globalen Datei fest, wie Codex mit dir kommuniziert (zum Beispiel Review-Stil, Ausführlichkeit und Standardeinstellungen), und beschränke Repository-spezifische Dateien auf Regeln für das Team und die Codebasis.

[Benutzerdefinierte Anweisungen mit AGENTS.md](/de-DE/codex/agent-configuration/agents-md)

## Skills

Skills erweitern Codex um wiederverwendbare Funktionen für wiederholbare Arbeitsabläufe.
Skills sind für wiederverwendbare Arbeitsabläufe oft die beste Wahl, weil sie umfangreichere Anweisungen, Skripte und Referenzen unterstützen und sich für verschiedene Aufgaben wiederverwenden lassen.
Skills werden geladen und sind für den Agenten sichtbar (zumindest ihre Metadaten). Dadurch kann Codex sie selbstständig finden und implizit auswählen. So bleiben umfangreiche Arbeitsabläufe verfügbar, ohne den Kontext gleich zu Beginn unnötig zu vergrößern.

Verwende Skill-Ordner, um Arbeitsabläufe lokal zu erstellen und weiterzuentwickeln. Wenn bereits ein Plug-in
für den Arbeitsablauf vorhanden ist, installiere es zuerst, um ein bewährtes Setup wiederzuverwenden. Wenn
du deinen eigenen Arbeitsablauf teamübergreifend verteilen oder mit
Konnektoren bündeln möchtest, verpacke ihn als [Plug-in](/de-DE/codex/build-plugins). Skills bleiben das
Format für die Erstellung; Plug-ins sind die installierbare Einheit für die Verteilung.

Ein Skill besteht in der Regel aus der Datei `SKILL.md` und optionalen Skripten, Referenzen sowie Assets.

Das Skill-Verzeichnis kann einen Ordner `scripts/` mit CLI-Skripten enthalten, die Codex im Rahmen des Arbeitsablaufs aufruft (zum Beispiel zum Einspielen von Ausgangsdaten oder zum Ausführen von Validierungen). Wenn der Arbeitsablauf externe Systeme benötigt (Issue-Tracker, Designtools, Dokumentationsserver), kombiniere den Skill mit [MCP](/de-DE/codex/extend/mcp).

Beispiel für `SKILL.md`:

```md
---
name: commit
description: Stage and commit changes in semantic groups. Use when the user wants to commit, organize commits, or clean up a branch before pushing.
---

1. Do not run `git add .`. Stage files in logical groups by purpose.
2. Group into separate commits: feat → test → docs → refactor → chore.
3. Write concise commit messages that match the change scope.
4. Keep each commit focused and reviewable.

Verwende Skills für:

- Wiederholbare Arbeitsabläufe (Schritte für Releases, Review-Routinen, Aktualisierungen der Dokumentation)
- Teamspezifisches Fachwissen
- Verfahren, die Beispiele, Referenzen oder Hilfsskripte erfordern

Skills können global (in deinem Benutzerverzeichnis, für deine persönliche Entwicklungsarbeit) oder Repository-spezifisch sein (für dein Team in `.agents/skills` eingecheckt). Lege Repository-Skills in `.agents/skills` ab, wenn der Arbeitsablauf für dieses Projekt gilt; verwende dein Benutzerverzeichnis für Skills, die dir in allen Repositorys zur Verfügung stehen sollen.

| Ebene  | Global               | Repository                                           |
| :----- | :------------------- | :--------------------------------------------- |
| AGENTS | `~/.codex/AGENTS.md` | `AGENTS.md` im Stammverzeichnis des Repositorys oder in untergeordneten Verzeichnissen |
| Skills | `~/.agents/skills`   | `.agents/skills` im Repository                       |

Codex lädt Skills schrittweise:

- Zunächst lädt Codex die Metadaten (`name`, `description`), um den Skill auffindbar zu machen
- Codex lädt `SKILL.md` erst, wenn ein Skill ausgewählt wurde
- Nur bei Bedarf liest Codex Referenzen oder führt Skripte aus

Skills können explizit aufgerufen werden. Codex kann sie auch implizit auswählen, wenn die Aufgabe zur Skill-Beschreibung passt. Mit klaren Skill-Beschreibungen funktioniert diese automatische Auswahl zuverlässiger.

[Skills erstellen](/de-DE/codex/build-skills)

## MCP

MCP (Model Context Protocol) ist das Standardverfahren, um Codex mit externen Tools und Kontextanbietern zu verbinden.
Besonders nützlich ist MCP bei remote gehosteten Systemen wie Figma, Linear, GitHub oder internen Wissensdiensten, auf die dein Team angewiesen ist.

Verwende MCP, wenn Codex auf Systeme außerhalb des lokalen Repositorys zugreifen muss, etwa auf Issue-Tracker, Designtools, Browser oder gemeinsam genutzte Dokumentationssysteme.

Du kannst es dir so vorstellen:

- **Host**: Codex
- **Client**: die MCP-Verbindung in Codex
- **Server**: das externe Tool oder der externe Kontextanbieter

MCP-Server können Folgendes bereitstellen:

- **Tools** (Aktionen)
- **Ressourcen** (lesbare Daten)
- **Prompts** (wiederverwendbare Prompt-Vorlagen)

Diese Trennung hilft dir, Vertrauensgrenzen und den jeweiligen Funktionsumfang besser einzuschätzen. Einige Server stellen hauptsächlich Kontext bereit, während andere weitreichende Aktionen ermöglichen.

In der Praxis ist MCP oft am nützlichsten, wenn du es mit Skills kombinierst:

- Ein Skill definiert den Arbeitsablauf und gibt an, welche MCP-Tools verwendet werden sollen

[Model Context Protocol](/de-DE/codex/extend/mcp)

## Subagenten

Du kannst verschiedene Agenten mit unterschiedlichen Rollen erstellen und sie anweisen, Tools jeweils anders einzusetzen. Beispielsweise kann ein Agent bestimmte Testbefehle ausführen und Konfigurationen anwenden, während ein anderer MCP-Server nutzt, die zur Fehlerbehebung Produktionslogs abrufen. Jeder Subagent konzentriert sich auf seine Aufgabe und verwendet die dafür passenden Tools.

[Subagenten](/de-DE/codex/agent-configuration/subagents)

## Skills und MCP im Zusammenspiel

Mit Skills und MCP greift alles ineinander: Skills definieren wiederholbare Arbeitsabläufe und MCP verbindet sie mit externen Tools und Systemen.
Wenn ein Skill von MCP abhängt, gib diese Abhängigkeit in `agents/openai.yaml` an, damit Codex sie automatisch installieren und einbinden kann (siehe [Skills erstellen](/de-DE/codex/build-skills)).

## Nächster Schritt

Setze deine Anpassung in dieser Reihenfolge um:

1. Lege [Benutzerdefinierte Anweisungen mit AGENTS.md](/de-DE/codex/agent-configuration/agents-md) fest, damit Codex die Konventionen deines Repositorys befolgt. Füge Pre-Commit-Hooks und Linter hinzu, um diese Regeln durchzusetzen.
2. Installiere ein [Plug-in](/de-DE/codex/plugins), wenn bereits ein wiederverwendbarer Arbeitsablauf vorhanden ist. Erstelle andernfalls einen [Skill](/de-DE/codex/build-skills) und verpacke ihn als Plug-in, wenn du ihn teilen möchtest.
3. Nutze [MCP](/de-DE/codex/extend/mcp), wenn Arbeitsabläufe externe Systeme benötigen (Linear, GitHub, Dokumentationsserver, Designtools).
4. Nutze [Subagenten](/de-DE/codex/agent-configuration/subagents), wenn du bereit bist, kontextlastige oder spezialisierte Aufgaben an Subagenten zu delegieren.

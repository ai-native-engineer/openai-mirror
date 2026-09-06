<!-- source: https://learn.chatgpt.com/de-DE/docs/build-skills -->

Verwende Agenten-Skills, um ChatGPT und Codex um aufgabenspezifische Funktionen zu erweitern. Ein
Skill bündelt Anweisungen, Ressourcen und optionale Skripte, damit beide Produkte
einen Ablauf zuverlässig ausführen können. Skills basieren auf dem
[offenen Standard für Agenten-Skills](https://agentskills.io).

Skills sind das Format zum Erstellen wiederverwendbarer Arbeitsabläufe. Plug-ins stellen
wiederverwendbare Skills und Konnektoren über das universelle Plug-in-Verzeichnis bereit, das
ChatGPT und Codex gemeinsam nutzen. Plug-ins funktionieren in Chat und Work in ChatGPT im Web,
auf dem Desktop und auf Mobilgeräten, in Codex in der ChatGPT-Desktop-App
und über Codex CLI. Entwirf mit Skills zunächst den Ablauf selbst und verpacke ihn als
[Plug-in](https://developers.openai.com/plugins/build/plugins), wenn
auch andere es installieren sollen.

Eigenständige Skills sind in der ChatGPT-Desktop-App, in Codex CLI und in der
IDE-Erweiterung verfügbar. In Plug-ins gebündelte Skills sind außerdem in Chat und Work
in ChatGPT im Web, auf dem Desktop und auf Mobilgeräten verfügbar.

Öffne in der ChatGPT-Desktop-App in der Seitenleiste **Skills** , um die in deinen Projekten erstellten Skills
anzuzeigen und zu erkunden.

  
    
  

Skills nutzen **schrittweise Offenlegung** , um den Kontext effizient zu verwalten. ChatGPT und
Codex beginnen mit dem Namen und der Beschreibung jedes Skills und laden die vollständigen
Anweisungen aus `SKILL.md` erst, wenn sie sich für die Verwendung des Skills entscheiden.

In Codex enthält die anfängliche Liste auch den Dateipfad jedes Skills. Damit sie
den übrigen Prompt nicht verdrängt, belegt sie höchstens 2 % des Kontextfensters
des Modells. Ist die Größe des Kontextfensters unbekannt, gilt eine Obergrenze von
8.000 Zeichen. Wenn viele Skills installiert sind, kürzt Codex zunächst ihre
Beschreibungen. Bei einer großen Zahl von Skills kann Codex einzelne Skills in der
anfänglichen Liste weglassen und eine Warnung anzeigen.

Dieses Budget gilt nur für die anfängliche Skills-Liste. Wählt Codex einen Skill aus, liest es dennoch dessen vollständige Anweisungen in SKILL.md.

Ein Skill ist ein Verzeichnis mit der Datei `SKILL.md` sowie optionalen Skripten und Referenzen. Die Datei `SKILL.md` muss `name` und `description` enthalten.

<a id="how-codex-uses-skills"></a>

## So verwenden ChatGPT und Codex Skills

ChatGPT und Codex können Skills auf zwei Arten aktivieren:

1. **Expliziter Aufruf:** Füge den Skill direkt in deinen Prompt ein. Gib in
   ChatGPT `@` ein, um einen Skill auszuwählen. Führe in Codex CLI oder der IDE-Erweiterung
`/skills` aus oder gib `$` ein, um einen Skill zu erwähnen.
2. **Impliziter Aufruf:** ChatGPT oder Codex kann einen Skill auswählen, wenn deine Aufgabe
   zur Beschreibung im Feld `description` des Skills passt.

Da der implizite Abgleich vom Feld `description` abhängt, verfasse prägnante Beschreibungen
mit einem klaren Anwendungsbereich und eindeutigen Grenzen. Nenne den wichtigsten Anwendungsfall und relevante Triggerwörter
gleich am Anfang, damit ein Host den Skill auch bei gekürzten Beschreibungen zuordnen kann.

## Skill erstellen

Wenn du den Ablauf bereits kennst und er sich leichter zeigen als beschreiben lässt, verwende
[„Aufzeichnen und Wiedergeben“](/de-DE/codex/extend/record-and-replay). Die Aufzeichnungsfunktion erfasst den
Ablauf, prüft die einzelnen Schritte und erstellt anhand der
Demonstration einen wiederverwendbaren Skill.

Wenn du den Skill lieber beschreiben möchtest, verwende den integrierten Erstellungsassistenten.
In ChatGPT Work rufst du ihn mit `@skill-creator` auf. In Codex lautet der Aufruf:

```text
$skill-creator

Der Erstellungsassistent fragt, was der Skill tut, wann er ausgelöst werden soll und ob er nur Anweisungen oder auch Skripte enthalten soll. Standardmäßig enthält der Skill nur Anweisungen.

Du kannst einen Skill auch manuell erstellen. Lege dazu einen Ordner mit der Datei `SKILL.md` an:

```md
---
name: skill-name
description: Explain exactly when this skill should and should not trigger.
---

Skill instructions for ChatGPT or Codex to follow.

Codex erkennt Änderungen an Skills automatisch. Wenn eine Aktualisierung nicht angezeigt wird, starte Codex neu.

<a id="where-to-save-skills"></a>

## Wo Codex lokale Skills lädt

Codex liest Skills aus Repository-, Benutzer-, Admin- und Systemverzeichnissen. In Repositories durchsucht Codex jedes Verzeichnis vom aktuellen Arbeitsverzeichnis bis zum Stammverzeichnis des Repositorys nach `.agents/skills`. Wenn zwei Skills für `name` denselben Wert haben, führt Codex sie nicht zusammen. Beide können in der Skill-Auswahl erscheinen.

| Geltungsbereich des Skills | Speicherort                                                                                                  | Empfohlene Verwendung                                                                                                                                                                                        |
| :---------- | :-------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `REPO`      | `$CWD/.agents/skills` <br /> Aktuelles Arbeitsverzeichnis: der Ordner, in dem du Codex startest.                           | Wenn du in einem Repository oder einer Codeumgebung arbeitest, können Teams Skills für einen bestimmten Arbeitsordner einchecken, etwa Skills, die nur für einen Microservice oder ein Modul relevant sind.                              |
| `REPO`      | `$CWD/../.agents/skills` <br /> Ein Ordner oberhalb von CWD, wenn du Codex in einem Git-Repository startest.         | In einem Repository mit verschachtelten Ordnern können Organisationen in einem übergeordneten Ordner Skills für einen gemeinsam genutzten Bereich einchecken.                                                                       |
| `REPO`      | `$REPO_ROOT/.agents/skills` <br /> Das oberste Stammverzeichnis, wenn du Codex in einem Git-Repository startest. | In einem Repository mit verschachtelten Ordnern können Organisationen Skills einchecken, die für alle relevant sind, die das Repository nutzen. Diese Skills stehen auf Stammebene in jedem Unterordner des Repositorys zur Verfügung. |
| `USER`      | `$HOME/.agents/skills` <br /> Alle Skills, die in deinem persönlichen Ordner eingecheckt sind.                         | Verwende diesen Speicherort, um für dich relevante Skills zu verwalten, die für jedes Repository gelten, in dem du arbeitest.                                                                                                           |
| `ADMIN`     | `/etc/codex/skills` <br /> Alle Skills, die auf dem Computer oder im Container in einem gemeinsam genutzten Systemverzeichnis eingecheckt sind. | Verwende diesen Speicherort für SDK-Skripte und Automatisierung sowie zum Einchecken standardmäßiger Admin-Skills, die allen auf dem Computer zur Verfügung stehen.                                                                                     |
| `SYSTEM`    | Von OpenAI zusammen mit Codex bereitgestellt.                                                                             | Nützliche Skills, die für viele relevant sind, etwa skill-creator und plan. Sie stehen allen beim Start von Codex zur Verfügung.                                                                   |

Codex unterstützt symbolisch verknüpfte Skill-Ordner und folgt beim Durchsuchen dieser Speicherorte dem Ziel der jeweiligen Verknüpfung.

Diese Speicherorte dienen zum Erstellen und lokalen Auffinden von Skills. Wenn du
wiederverwendbare Skills über ein einzelnes Repository hinaus verteilen oder sie optional mit
Konnektoren bündeln möchtest, verwende [Plug-ins](https://developers.openai.com/plugins/build/plugins).

## Skills mit Plug-ins verteilen

Direkte Skill-Ordner eignen sich am besten zum lokalen Erstellen und für Arbeitsabläufe innerhalb eines Repositorys. Wenn
du einen wiederverwendbaren Skill verteilen, mindestens zwei Skills bündeln oder
einen Skill zusammen mit einem Konnektor bereitstellen möchtest, erstelle daraus ein
[Plug-in](https://developers.openai.com/plugins/build/plugins).

Plug-ins können einen oder mehrere Skills enthalten. Optional können sie auch
registrierte Verbindungen zu MCP-Servern, eine gebündelte MCP-Server-Konfiguration
und Ressourcen für die Darstellung in einem einzigen Paket zusammenfassen.

## Ausgewählte Skills für die lokale Nutzung installieren

Um deinem lokalen Codex-Setup neben den integrierten Skills weitere ausgewählte Skills hinzuzufügen, verwende `$skill-installer`. So installierst du beispielsweise den Skill `$linear`:

```bash
$skill-installer linear

Du kannst das Installationsprogramm auch per Prompt anweisen, Skills aus anderen Repositories
herunterzuladen. Codex erkennt neu installierte Skills automatisch. Sollte ein Skill nicht angezeigt werden,
starte Codex neu.

Nutze diese Möglichkeit für das lokale Setup und zum Experimentieren. Um eigene Skills
zur Wiederverwendung zu verteilen, solltest du Plug-ins bevorzugen.

## Lokale Codex-Skills aktivieren oder deaktivieren

Verwende Einträge vom Typ `[[skills.config]]` in `~/.codex/config.toml`, um einen Skill zu deaktivieren, ohne ihn zu löschen:

```toml
[[skills.config]]
path = "/path/to/skill/SKILL.md"
enabled = false

Starte Codex neu, nachdem du `~/.codex/config.toml` geändert hast.

## Optionale Metadaten

Füge `agents/openai.yaml` hinzu, um UI-Metadaten in der [ChatGPT-Desktop-App](/de-DE/codex/app) zu konfigurieren, Aufrufregeln festzulegen und Tool-Abhängigkeiten zu deklarieren. So lässt sich der Skill reibungsloser verwenden.

```yaml
interface:
  display_name: "Optional user-facing name"
  short_description: "Optional user-facing description"
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
  brand_color: "#3B82F6"
  default_prompt: "Optional surrounding prompt to use the skill with"

policy:
  allow_implicit_invocation: false

dependencies:
  tools:
    - type: "mcp"
      value: "openaiDeveloperDocs"
      description: "OpenAI Docs MCP server"
      transport: "streamable_http"
      url: "https://developers.openai.com/mcp"

`allow_implicit_invocation` (Standard: `true`): Bei `false` ruft Codex den Skill nicht implizit anhand des eingegebenen Prompts auf. Der explizite Aufruf mit `$skill` funktioniert weiterhin.

## Bewährte Methoden

- Beschränke jeden Skill auf eine Aufgabe.
- Bevorzuge Anweisungen gegenüber Skripten, außer wenn du deterministisches Verhalten oder externe Tools benötigst.
- Formuliere die Schritte im Imperativ und gib Ein- und Ausgaben ausdrücklich an.
- Teste Prompts anhand der Skill-Beschreibung, um sicherzustellen, dass der Skill wie vorgesehen ausgelöst wird.

Weitere Beispiele findest du unter
[GitHub-CI-Reparatur](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci),
[PDF](https://github.com/openai/skills/tree/main/skills/.curated/pdf),
[Linear](https://github.com/openai/skills/tree/main/skills/.curated/linear),
[openai/skills](https://github.com/openai/skills) und in der
[Spezifikation für Agenten-Skills](https://agentskills.io/specification). Für die
Verteilung installierbarer Skills verwende bevorzugt [Plug-ins](https://developers.openai.com/plugins/build/plugins).

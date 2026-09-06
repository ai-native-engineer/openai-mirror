<!-- source: https://learn.chatgpt.com/de-DE/docs/agent-configuration/agents-md -->

Codex liest vor Beginn jeder Aufgabe die Dateien namens `AGENTS.md`. Indem du globale Anweisungen mit projektspezifischen Überschreibungen kombinierst, gelten für jede Aufgabe von Anfang an dieselben Erwartungen, unabhängig davon, welches Repository du öffnest.

## So ermittelt Codex die Anweisungen

Beim Start erstellt Codex eine Anweisungskette (einmal pro Ausführung; in der TUI bedeutet das normalerweise einmal pro gestarteter Sitzung). Für die Ermittlung gilt diese Prioritätsreihenfolge:

1. **Globaler Geltungsbereich:** In deinem Codex-Stammverzeichnis (standardmäßig `~/.codex`, sofern du nicht `CODEX_HOME` festlegst) liest Codex `AGENTS.override.md`, falls die Datei vorhanden ist. Andernfalls liest Codex `AGENTS.md`. Auf dieser Ebene verwendet Codex nur die erste nicht leere Datei.
2. **Geltungsbereich des Projekts:** Vom Projektstammverzeichnis (meist dem Git-Stammverzeichnis) aus durchsucht Codex den Pfad bis zu deinem aktuellen Arbeitsverzeichnis. Wenn Codex kein Projektstammverzeichnis findet, prüft es nur das aktuelle Verzeichnis. In jedem Verzeichnis entlang des Pfads sucht es zuerst nach `AGENTS.override.md`, dann nach `AGENTS.md` und schließlich nach alternativen Namen aus `project_doc_fallback_filenames`. Codex berücksichtigt höchstens eine Datei pro Verzeichnis.
3. **Reihenfolge beim Zusammenführen:** Codex fügt die Dateien vom Stammverzeichnis abwärts zusammen und trennt sie durch Leerzeilen. Dateien, die näher an deinem aktuellen Verzeichnis liegen, überschreiben frühere Anweisungen, da sie im zusammengeführten Prompt später stehen.

Codex überspringt leere Dateien und fügt keine weiteren hinzu, sobald die Gesamtgröße den durch `project_doc_max_bytes` festgelegten Grenzwert erreicht (standardmäßig 32 KiB). Weitere Informationen zu diesen Einstellungen findest du unter [Ermittlung von Projektanweisungen](/de-DE/codex/config-file/config-advanced#project-instructions-discovery). Erhöhe den Grenzwert oder verteile die Anweisungen auf verschachtelte Verzeichnisse, wenn du ihn erreichst.

## Globale Anweisungen erstellen

Lege dauerhafte Standardvorgaben in deinem Codex-Stammverzeichnis fest, damit jedes Repository deine Arbeitskonventionen übernimmt.

1. Stelle sicher, dass das Verzeichnis vorhanden ist:

   ```bash
   mkdir -p ~/.codex

2. Erstelle `~/.codex/AGENTS.md` mit wiederverwendbaren Vorgaben:

   ```md
   # ~/.codex/AGENTS.md

   ## Working agreements

   - Always run `npm test` after modifying JavaScript files.
   - Prefer `pnpm` when installing dependencies.
   - Ask for confirmation before adding new production dependencies.

3. Starte Codex in einem beliebigen Verzeichnis, um zu prüfen, ob die Datei geladen wird:

   ```bash
   codex --ask-for-approval never "Summarize the current instructions."

   Erwartetes Ergebnis: Codex gibt die Einträge aus `~/.codex/AGENTS.md` wieder, bevor es Arbeitsschritte vorschlägt.

Verwende `~/.codex/AGENTS.override.md`, wenn du die globalen Anweisungen vorübergehend überschreiben möchtest, ohne die Basisdatei zu löschen. Entferne die Override-Datei, um die gemeinsamen Anweisungen wiederherzustellen.

## Projektanweisungen hierarchisch ergänzen

Dateien auf Repository-Ebene sorgen dafür, dass Codex die Projektkonventionen berücksichtigt und zugleich deine globalen Standardvorgaben übernimmt.

1. Füge im Stammverzeichnis deines Repositorys eine Datei namens `AGENTS.md` hinzu, die das grundlegende Setup beschreibt:

   ```md
   # AGENTS.md

   ## Repository expectations

   - Run `npm run lint` before opening a pull request.
   - Document public utilities in `docs/` when you change behavior.

2. Füge in verschachtelten Verzeichnissen Override-Dateien hinzu, wenn einzelne Teams abweichende Regeln benötigen. Erstelle beispielsweise in `services/payments/` die Datei `AGENTS.override.md`:

   ```md
   # services/payments/AGENTS.override.md

   ## Payments service rules

   - Use `make test-payments` instead of `npm test`.
   - Never rotate API keys without notifying the security channel.

3. Starte Codex im payments-Verzeichnis:

   ```bash
   codex --cd services/payments --ask-for-approval never "List the instruction sources you loaded."

   Erwartetes Ergebnis: Codex nennt zuerst die globale Datei, dann `AGENTS.md` im Repository-Stammverzeichnis und zuletzt die payments-spezifische Override-Datei.

Codex beendet die Suche, sobald es dein aktuelles Verzeichnis erreicht. Lege Override-Dateien daher möglichst nah an dem Bereich ab, für den die speziellen Regeln gelten.

So sieht ein Beispiel-Repository aus, nachdem du eine globale Datei und eine payments-spezifische Override-Datei hinzugefügt hast:

## Regeln für Code Reviews hinzufügen

Wenn du [Code Review mit Codex in GitHub](/de-DE/codex/third-party/github#customize-what-codex-reviews) verwendest,
füge den Abschnitt `## Code Review Rules` in der Datei `AGENTS.md` hinzu, die dem Code am nächsten liegt, für den die
Regeln gelten. Lege Repository-weite Prüfungen im Stammverzeichnis und dienstspezifische
Prüfungen in einer verschachtelten Datei ab.

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Formuliere Regeln knapp, beschreibe das zu beanstandende Verhalten sowie eine sichere Vorgehensweise oder
Ausnahme und überlasse Formatierungs- und Lint-Prüfungen der CI. Unter [Anpassen, was
Codex überprüft](/de-DE/codex/third-party/github#customize-what-codex-reviews) findest du Hinweise für
das Setup und das Verfassen von Regeln.

## Alternative Dateinamen anpassen

Wenn dein Repository bereits einen anderen Dateinamen verwendet (zum Beispiel `TEAM_GUIDE.md`), füge ihn der Liste alternativer Dateinamen hinzu, damit Codex die Datei wie eine Anweisungsdatei behandelt.

1. Bearbeite deine Codex-Konfiguration:

   ```toml
   # ~/.codex/config.toml
   project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
   project_doc_max_bytes = 65536

2. Starte Codex neu oder führe einen neuen Befehl aus, damit die aktualisierte Konfiguration geladen wird.

Nun prüft Codex jedes Verzeichnis in dieser Reihenfolge: `AGENTS.override.md`, `AGENTS.md`, `TEAM_GUIDE.md`, `.agents.md`. Dateinamen, die nicht in dieser Liste stehen, werden bei der Ermittlung von Anweisungen ignoriert. Der höhere Grenzwert erlaubt es, mehr Anweisungen zusammenzuführen, bevor sie abgeschnitten werden.

Mit der Liste alternativer Dateinamen behandelt Codex auch diese Dateien als Anweisungen:

Lege die Umgebungsvariable `CODEX_HOME` fest, wenn du ein anderes Profil verwenden möchtest, beispielsweise das eines projektspezifischen Benutzerkontos für Automatisierungen:

```bash
CODEX_HOME=$(pwd)/.codex codex exec "List active instruction sources"

Erwartetes Ergebnis: Die Ausgabe listet die Dateien relativ zum benutzerdefinierten Verzeichnis `.codex` auf.

## Setup überprüfen

- Führe `codex --ask-for-approval never "Summarize the current instructions."` im Stammverzeichnis eines Repositorys aus. Codex sollte die Anweisungen aus globalen Dateien und Projektdateien in Prioritätsreihenfolge wiedergeben.
- Prüfe mit `codex --cd subdir --ask-for-approval never "Show which instruction files are active."`, ob verschachtelte Override-Dateien allgemeinere Regeln ersetzen.
- Um zu prüfen, welche Anweisungsdateien Codex geladen hat, aktiviere mit `codex -c log_dir=./.codex-log` ein TUI-Protokoll im Klartext und prüfe `./.codex-log/codex-tui.log`, oder sieh dir die neueste Datei nach dem Muster `session-*.jsonl` an, wenn du die Sitzungsprotokollierung aktiviert hast.
- Wenn die Anweisungen veraltet wirken, starte Codex im Zielverzeichnis neu. Codex erstellt die Anweisungskette bei jeder Ausführung (und zu Beginn jeder TUI-Sitzung) neu. Daher musst du keinen Cache manuell leeren.

## Probleme beim Ermitteln von Anweisungen beheben

- **Nichts wird geladen:** Prüfe, ob du dich im vorgesehenen Repository befindest und `codex status` das erwartete Workspace-Stammverzeichnis meldet. Stelle sicher, dass die Anweisungsdateien Inhalt enthalten; Codex ignoriert leere Dateien.
- **Falsche Anweisungen werden geladen:** Suche weiter oben im Verzeichnisbaum oder in deinem Codex-Stammverzeichnis nach einer Datei namens `AGENTS.override.md`. Benenne die Override-Datei um oder entferne sie, damit Codex wieder die reguläre Datei verwendet.
- **Codex ignoriert alternative Dateinamen:** Prüfe, ob du die Namen fehlerfrei in `project_doc_fallback_filenames` eingetragen hast. Starte Codex anschließend neu, damit die aktualisierte Konfiguration wirksam wird.
- **Anweisungen werden abgeschnitten:** Erhöhe `project_doc_max_bytes` oder teile umfangreiche Anweisungen auf Dateien in verschachtelten Verzeichnissen auf, damit wichtige Anweisungen vollständig erhalten bleiben.
- **Profil unklar:** Führe `echo $CODEX_HOME` aus, bevor du Codex startest. Bei einem Wert, der vom Standard abweicht, verwendet Codex ein anderes Stammverzeichnis als das von dir bearbeitete.

## Nächste Schritte

- Weitere Informationen findest du auf der offiziellen Website zu [AGENTS.md](https://agents.md).
- Unter [Prompting für Codex](/de-DE/codex/prompting) findest du Dialogmuster, die sich gut mit dauerhaften Anweisungen kombinieren lassen.

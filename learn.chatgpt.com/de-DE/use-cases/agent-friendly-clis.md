<!-- source: https://learn.chatgpt.com/de-DE/use-cases/agent-friendly-clis -->

## Einführung

Wenn Codex immer wieder mit einer bestimmten API, Protokollquelle, einem exportierten Postfach, einer lokalen Datenbank oder einem Team-Skript arbeitet, stelle dafür eine flexibel kombinierbare Schnittstelle bereit: einen Befehl, den Codex aus jedem Ordner ausführen und mit `git`, `gh`, `rg`, Tests und Repository-Skripten kombinieren kann und dessen Ergebnisse sich prüfen und eingrenzen lassen.

Füge einen zugehörigen Skill hinzu, der festhält, wann Codex die CLI verwenden soll, was zuerst auszuführen ist, wie sich die Ausgabe begrenzen lässt, wo heruntergeladene Dateien gespeichert werden und welche Schreibbefehle eine Genehmigung erfordern.

In diesem Workflow hilft `$cli-creator` Codex dabei, den Befehl zu entwickeln. Mit `$skill-creator` kann Codex einen wiederverwendbaren Skill wie `$ci-logs` speichern, der sich bei späteren Aufgaben anhand seines Namens aufrufen lässt.

## Anwendung

1. [Entscheide, ob die Aufgabe eine CLI braucht](#choose-what-the-cli-should-do)
2. [Stelle die Quelle bereit, die Codex auswerten soll](#share-the-docs-files-or-commands)
3. [Führe `$cli-creator` aus](#ask-codex-to-build-the-cli-and-skill)
4. [Teste den installierten Befehl](#verify-the-command-works-from-any-folder)
5. [Rufe den gespeicherten Skill später auf](#use-the-skill-later)

## Lege fest, was die CLI tun soll

Beginne mit dem, was Codex tun soll, nicht mit der Technologie, die Codex dafür entwickeln soll. Eine gute CLI verpackt wiederkehrende Vorgänge wie Lesen, Suchen, Herunterladen, Exportieren, Entwerfen, Hochladen, Statusabfragen oder sicheres Schreiben in einen Befehl, den Codex aus jedem Repository ausführen kann.

| Situation                                              | Was Codex mit der CLI tun kann                                                                                              |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| **CI-Protokolle sind nur über eine Build-Seite zugänglich.**                  | Eine Build-URL übernehmen, die Protokolle fehlgeschlagener Jobs nach `./logs` herunterladen und Dateipfade sowie kurze Ausschnitte zurückgeben.                          |
| **Supporttickets werden wöchentlich exportiert.**         | Den neuesten CSV- oder JSON-Export indexieren, nach Kundennamen oder Formulierungen suchen und ein einzelnes Ticket anhand einer stabilen ID lesen.                        |
| **Eine API-Antwort ist zu groß für den Kontext.**          | Nur die benötigten Felder auflisten, das vollständige Objekt anhand seiner ID lesen und die gesamte Antwort in eine Datei exportieren.                      |
| **Ein Slack-Export enthält lange Threads.**                   | Mit `--limit` suchen, einen einzelnen Thread lesen und den umgebenden Kontext statt des gesamten Archivs zurückgeben.                             |
| **Ein Team-Skript umfasst vier verschiedene Schritte.**           | Setup, Suche, Download, Entwurf, Upload, Statusabfrage und direktes Schreiben in separate Befehle aufteilen.                               |
| **Ein Plug-in findet den Datensatz, aber Codex benötigt eine Datei.** | Das Plug-in weiterhin im Chat verwenden und eine CLI nutzen, um den Anhang, Trace, Bericht, das Video oder Protokollpaket herunterzuladen und den Pfad zurückzugeben. |

## Dokumentation, Dateien oder Befehle bereitstellen

Codex braucht konkrete Inhalte, die es auswerten kann: eine Dokumentation oder OpenAPI-Spezifikation, einen um vertrauliche Angaben bereinigten curl-Befehl, den Pfad zu einem Export oder einer Datenbank, einen Protokollordner oder ein vorhandenes Skript. Wenn die CLI einem vertrauten Stil folgen soll, füge eine kurze Ausgabe ein, die `gh`, `kubectl` oder das Tool deines Teams mit `--help` erzeugt.

Wenn der Befehl eine Authentifizierung erfordert, teile Codex den Namen der Umgebungsvariable, den Pfad zur Konfigurationsdatei oder das Anmeldeverfahren mit, das die CLI unterstützen soll. Hinterlege den geheimen Wert selbst in deiner Shell oder Konfigurationsdatei. Füge keine geheimen Werte in den Chat ein. Bitte Codex, die Setup-Prüfung der CLI bei fehlender Authentifizierung mit einer klaren Fehlermeldung abbrechen zu lassen.

## Bitte Codex, die CLI und den Skill zu entwickeln

Verwende den Start-Prompt auf dieser Seite. Gib die Quelle an, die Codex auswerten soll, sowie die erste Aufgabe, die die CLI unterstützen soll.

Bevor Codex Code schreibt, soll es die vorgeschlagene Befehlsstruktur zeigen und nur nach fehlenden Angaben fragen, ohne die die Entwicklung nicht möglich ist.

## Prüfe, ob der Befehl aus jedem Ordner funktioniert

Codex sollte nicht schon nach `cargo run`, `python path/to/script.py` oder einem Befehl für ein nicht installiertes Paket aufhören. Bitte Codex, den installierten Befehl aus einem anderen Repository oder einem temporären Ordner so zu testen, wie ihn eine spätere Aufgabe verwenden wird.

**Teste die CLI so, wie es ein zukünftiger Agent tun würde**

Wenn Codex einen riesigen JSON-Datenblock zurückgibt, bitte es, die Standardantwort stärker einzugrenzen und einen Dateiexport für vollständige Payloads hinzuzufügen. Falls Codex vergisst, welche Schreibaktionen eine Genehmigung erfordern, bitte es, den zugehörigen Skill zu aktualisieren, bevor du ihn für eine weitere Aufgabe verwendest.

## Skill später verwenden

Wenn du die CLI wieder brauchst, rufe den Skill auf, statt die Dokumentation erneut einzufügen:

Teste den Skill bei wiederkehrenden Aufgaben zunächst einmal in einem Chat und bitte Codex dann, [für denselben Aufruf direkt aus dem Chat eine Aufgabe zu planen](/de-DE/codex/automations#schedule-a-task-inside-a-chat).

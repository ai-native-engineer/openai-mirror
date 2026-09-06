<!-- source: https://learn.chatgpt.com/de-DE/docs/long-running-work -->

Gib ChatGPT für Aufgaben, die viele Schritte erfordern können, ein klar definiertes Ergebnis, Einschränkungen
und eindeutige Abschlusskriterien vor. Bearbeite zusammengehörige Aufgaben im selben Chat, damit
ChatGPT denselben Kontext nutzen kann, um den nächsten Schritt auszuwählen und festzustellen, wann die
Aufgabe abgeschlossen ist.

Gib in der ChatGPT-Desktop-App `/goal` ein, um den Zielmodus zu starten. Über die Fortschrittszeile
kannst du das Ziel pausieren, fortsetzen, bearbeiten oder löschen, während ChatGPT daran arbeitet.

Verwende für gehostete, lang laufende Aufgaben in der Webversion von ChatGPT ChatGPT Work und gib das
Ergebnis, die Einschränkungen und die Prüfkriterien direkt in deinem Prompt an.

Führe denselben Web-Chat fort, um Kontext hinzuzufügen, Einschränkungen zu ändern oder
nach dem aktuellen Stand zu fragen. Nutze separate Chats, wenn unabhängige Aufgaben
parallel ausgeführt werden können, und vermeide, dass zwei Aufgaben Schreibzugriff auf dieselbe angebundene Quelle erhalten.
Fasse bei zusammengehörigen Aufgaben Chats und Quelldateien in einem
[Projekt](/de-DE/codex/projects) zusammen.

Gib in einer interaktiven Sitzung der Codex CLI `/goal` ein, um den Zielmodus zu starten. Setze
dieselbe Sitzung fort, um die Arbeit zu steuern oder nach dem aktuellen Stand zu fragen.

Gib im Chat der IDE-Erweiterung `/goal` ein, um den Zielmodus für den geöffneten
Workspace zu starten. Führe denselben Chat fort, um die Aufgabe während der Ausführung zu steuern.

  
    
  

<a id="start-a-goal"></a>
<a id="define-what-done-means"></a>
<a id="steer-a-running-goal"></a>
<a id="run-goals-in-parallel"></a>
<a id="related-docs"></a>

## Ein Ziel starten

Gib `/goal` in der ChatGPT-Desktop-App, in der Codex CLI oder in der IDE-Erweiterung ein. Der
Zieltext ist zugleich der erste Prompt und legt die Abschlusskriterien für die
Aufgabe fest.

Wenn das gewünschte Ergebnis noch unklar ist, beginne mit `/plan`. Bitte ChatGPT, dich zu befragen,
Einschränkungen zu ermitteln und daraus ein Ziel mit messbaren
Erfolgskriterien zu formulieren. Starte das präzisierte Ziel anschließend mit `/goal`.

## Lege fest, wann die Aufgabe abgeschlossen ist

Formuliere ein Ziel, mit dem ChatGPT den eigenen Fortschritt überprüfen kann. Berücksichtige drei Punkte, sofern
sie relevant sind:

| Bestandteil des Ziels     | Erforderliche Angaben                                                               |
| ---------------- | ----------------------------------------------------------------------------- |
| **Ergebnis**      | Beschreibe das gewünschte Ergebnis, nicht nur, was ChatGPT tun soll.   |
| **Einschränkungen**  | Nenne erforderliche Tools, einzuhaltende Grenzen, Kompatibilitätsanforderungen oder Vorgehensweisen, die vermieden werden sollen. |
| **Überprüfung** | Füge Tests, Messungen oder Prüfkriterien hinzu, die belegen, dass die Aufgabe abgeschlossen ist.  |

Zum Beispiel:

```text
Migrate this codebase from JavaScript to TypeScript. Preserve existing behavior,
compile in strict mode without explicit `any` types, and make the full test suite pass.

## Ein laufendes Ziel steuern

In der ChatGPT-Desktop-App wird die Fortschrittszeile für das Ziel oberhalb des Editors angezeigt. Damit kannst du die Arbeit
pausieren oder fortsetzen und das Ziel bearbeiten oder löschen. Während das Ziel läuft, kannst du außerdem weitere
Nachrichten senden, um Kontext hinzuzufügen oder Einschränkungen anzupassen.

Nutze einen Nebenchat, wenn du eine Statusübersicht oder eine Erklärung möchtest, ohne
den Hauptchat zu unterbrechen. Pausiere das Ziel, bevor du voraussichtlich die
Verbindung verlierst, und setze es fort, sobald ChatGPT weiterarbeiten soll.

<a id="steer-a-running-task"></a>

## Laufende Aufgaben steuern

Führe denselben Chat fort, um Kontext hinzuzufügen, Einschränkungen anzupassen oder
eine Statusübersicht anzufordern. Starte einen separaten Chat, wenn eine andere Aufgabe
unabhängig ausgeführt werden kann.

## Ein laufendes Ziel steuern

Sende in derselben interaktiven Sitzung eine weitere Nachricht, um Kontext hinzuzufügen oder
Einschränkungen anzupassen. Fordere eine Statusübersicht an, wenn Codex vor dem
Weiterarbeiten den bisherigen Fortschritt zusammenfassen soll.

## Ein laufendes Ziel steuern

Führe denselben IDE-Chat fort, um Kontext hinzuzufügen, Einschränkungen anzupassen oder eine
Statusübersicht anzufordern. Sorge dafür, dass der Workspace verfügbar bleibt, solange das Ziel läuft.

Das Starten eines Ziels erweitert die Zugriffsrechte von ChatGPT nicht. ChatGPT arbeitet weiterhin mit derselben
[Sandbox und Genehmigungsrichtlinie](/de-DE/codex/sandboxing) und pausiert, wenn
eine Entscheidung erforderlich ist. Mit [automatischen Prüfungen von
Genehmigungsanfragen](/de-DE/codex/sandboxing/auto-review) kann eine separate Prüfinstanz
dafür infrage kommende Anfragen prüfen, ohne diese Grenzen auszuweiten.

## Ziele parallel ausführen

Jeder Chat behält seinen eigenen Kontext, seine Nachrichten, seine Ergebnisse und sein Ziel. Führe Chats
parallel aus, aber vermeide, dass zwei Chats dieselben Dateien ändern. Nutze
[Worktrees](/de-DE/codex/environments/git-worktrees), damit parallel laufende Chats für Programmieraufgaben jeweils einen eigenen
Checkout verwenden.

Aktiviere für lokale Aufgaben in den Einstellungen **Ruhezustand während der Ausführung verhindern** , damit dein Mac
nicht in den Ruhezustand wechselt. Nutze [Begleiter](/de-DE/codex/pets?surface=app) oder [Benachrichtigungen des
Systems](/de-DE/codex/notifications?surface=app), um zu erkennen, wann ein Chat eine Eingabe benötigt
oder zur Überprüfung bereit ist.

## Weitere Dokumentation

- [Projekte und Chats](/de-DE/codex/projects)
- [Zielmodus und Prompting](/de-DE/codex/prompting#goal-mode)
- [Git-Worktrees](/de-DE/codex/environments/git-worktrees)

## Weitere Dokumentation

- [Projekte und Chats](/de-DE/codex/projects)
- [Geplante Aufgaben](/de-DE/codex/automations)
- [Sandbox und Berechtigungen](/de-DE/codex/sandboxing)

<!-- source: https://learn.chatgpt.com/de-DE/docs/prompting -->

<a id="prompts"></a>

## Übersicht zum Prompting

Beim Prompting teilst du ChatGPT mit, was du wissen, erstellen oder ändern möchtest. Ein Prompt
kann eine Frage, eine Anweisung oder ein Ziel sein. Du brauchst weder technische Syntax noch
eine starre Formel. Formuliere dein Anliegen in eigenen Worten, prüfe die Antwort und gestalte das Ergebnis mit
Folgenachrichten.

Ein kurzer Prompt reicht oft aus. Füge bei umfangreicheren oder wichtigeren Aufgaben die
entscheidenden Bestandteile hinzu:

- **Ziel:** Was soll ChatGPT tun?
- **Kontext:** Welche Informationen oder Quellen sind hilfreich?
- **Ausgabe:** Welches Format, welche Länge oder welchen Detailgrad brauchst du?
- **Grenzen:** Was muss unverändert bleiben? Was soll ChatGPT vermeiden oder vor dem Handeln
  mit dir abstimmen?

Verwende nur die Bestandteile, die hilfreich sind. Du musst nicht jeden Punkt berücksichtigen oder einem
vorgegebenen Format folgen.

## Beschreibe das gewünschte Ergebnis

Beginne mit dem Ergebnis, nicht mit einer detaillierten Liste von Schritten. Nenne die Zielgruppe oder das
Format, wenn diese Angaben beeinflussen, was ChatGPT erstellen soll.

```text
Turn these meeting notes into a short update for the project team.
Put the decisions and next steps first.

Dieser Prompt erklärt, was erstellt werden soll und für wen es bestimmt ist. Beschreibe einen Ablauf, wenn
er selbst wichtig ist. Lass ChatGPT andernfalls genügend Spielraum, um zu suchen, Informationen zu vergleichen
und seine Vorgehensweise anzupassen.

<a id="context"></a>

## Füge hilfreichen Kontext hinzu

Stelle Informationen bereit, die das Ergebnis beeinflussen könnten. Füge nur relevante Quellen
hinzu und erkläre, was ChatGPT jeweils daraus entnehmen soll.

- Hänge Dokumente, Tabellen, Präsentationen oder PDF-Dateien an, wenn du möchtest, dass
  ChatGPT sie zusammenfasst, vergleicht, umwandelt oder [Dateien zur Überprüfung erstellt](/de-DE/codex/artifacts-viewer).
- Füge einen Screenshot, ein Diagramm oder eine andere [Bildeingabe](/de-DE/codex/image-inputs) hinzu, wenn die
  Aufgabe visuellen Kontext erfordert. Weise auf den relevanten Bereich hin, statt dich
  allein auf das Bild zu verlassen.
- Bitte ChatGPT, die [Websuche](/de-DE/codex/web-search) zu verwenden, wenn die Antwort von
  aktuellen Informationen abhängt, und fordere Quellen an, wenn du das Ergebnis überprüfen musst.
- Verwende ein [Projekt](/de-DE/codex/projects), wenn zusammengehörige Chats Dateien,
  Quellen oder einen lokalen Ordner gemeinsam nutzen sollen.

### Verbundene Quellen verwenden

Wenn ChatGPT auf verbundene Quellen zugreifen kann, gib an, wo es suchen und was
es finden soll. Du musst nicht jede einzelne Suche beschreiben.

```text
Use the latest project plan in Drive and relevant decisions and updates from
the project's Slack channel to prepare a status update.

Verbundene Quellen erfordern das passende Plug-in. Ihre Verfügbarkeit kann von
deinem Tarif und den Workspace-Einstellungen abhängen.

### Plug-ins verwenden

Plug-ins stellen ChatGPT und Codex wiederverwendbare Anweisungen und Verbindungen zu Tools
wie Google Drive, Gmail, Slack und GitHub bereit. Beide Produkte beziehen öffentliche
Plug-ins aus demselben universellen Verzeichnis. Beschreibe das gewünschte Ergebnis und überlasse
der aktiven Oberfläche die Auswahl unter den verfügbaren Tools. Gib in ChatGPT `@`
in den Editor ein, um ein bestimmtes Plug-in auszuwählen.

  
    <span slot="icon">
      
    </span>
    Finde, installiere und verwende Plug-ins in ChatGPT und Codex.
  

### ChatGPT personalisieren

Lege Präferenzen, die für alle Chats gelten sollen, unter **Einstellungen \> Personalisierung**
als benutzerdefinierte Anweisungen fest. Details, die nur für den aktuellen Chat relevant sind, gehören in den
Prompt.

  
    <span slot="icon">
      
    </span>
    Lege eine Standardpersönlichkeit, benutzerdefinierte Anweisungen und weitere App-Einstellungen fest.
  

## Setze Grenzen, um konkrete Probleme zu vermeiden

Grenzen sind die wenigen Anweisungen, die ChatGPT braucht, um zusätzliche Arbeit
oder unbeabsichtigte Handlungen zu vermeiden. Lege eine Grenze fest, wenn eine Änderung an der falschen Stelle
das Ergebnis unbrauchbar machen würde oder wenn du etwas prüfen möchtest, bevor es sich auf
andere auswirkt.

- Lass die freigegebenen Termine und Budgetzahlen unverändert.
- Verwende nur die bereitgestellten Quellen. Weise auf fehlende Informationen hin, statt Vermutungen anzustellen.
- Achte darauf, dass die Empfehlungen das angegebene Budget nicht überschreiten.
- Bereite die Nachricht als Entwurf vor. Sende sie nicht.

Konzentriere dich auf die ein oder zwei wichtigsten Grenzen. Du musst nicht jeden
Schritt von ChatGPT kontrollieren.

## Sorge dafür, dass das Ergebnis direkt nutzbar ist

Erkläre ChatGPT, wie du das Ergebnis verwenden möchtest. So kann es die passende
Länge, den richtigen Detailgrad und eine geeignete Struktur wählen.

- Erstelle eine einseitige Zusammenfassung, die Personen auf Director-Ebene vor dem Meeting überfliegen können. Stelle die
Entscheidung und die nächsten Schritte an den Anfang.
- Formuliere aus diesen Notizen eine E-Mail zur Nachbereitung mit den Entscheidungen, den zuständigen Personen und den
Fälligkeitsterminen.
- Erstelle eine übersichtliche Tabelle, die geplante und tatsächliche Ausgaben gegenüberstellt, und hebe jede
Abweichung von mehr als 10 % hervor.

Bitte ChatGPT bei wichtigen Aufgaben um eine abschließende Prüfung. Es soll zum Beispiel bestätigen, dass für jede
Aufgabe eine zuständige Person und ein Fälligkeitstermin angegeben sind, oder Informationen kennzeichnen, die es nicht
überprüfen konnte. Prüfe das Ergebnis anschließend selbst, bevor du es verwendest oder weitergibst.

## Verbessere das Ergebnis mit Folgenachrichten

Dein erster Prompt muss nicht perfekt sein. Prüfe das Ergebnis und beschreibe anschließend konkret,
was du ändern möchtest.

```text
Make the opening more direct, keep the evidence, and move the recommendation
above the background section.

Du kannst eine fehlende Quelle ergänzen, die Richtung korrigieren, um eine weitere Option bitten oder
den Detailgrad ändern, ohne neu anfangen zu müssen.

### Steuern und Einreihen

Wenn Codex bereits arbeitet, kannst du eine weitere Nachricht senden, ohne auf den Abschluss
der aktuellen Ausführung zu warten:

- **Steuern** fügt die Nachricht der aktuellen Ausführung hinzu. Nutze diese Option, um die Richtung zu ändern,
  ein fehlendes Detail zu ergänzen oder neue Informationen bereitzustellen.
- **Einreihen** speichert die Nachricht für die nächste Ausführung. Nutze diese Option für eine Folgenachricht, die
  warten soll, bis die aktuelle Arbeit abgeschlossen ist.

Lege in der ChatGPT-Desktop-App die Standardeinstellung unter
[**Einstellungen \> Allgemein \> Verhalten bei Folgenachrichten**](/de-DE/codex/app/settings#general) fest.
Eingereihte Nachrichten erscheinen über dem Editor. Dort kannst du sie bearbeiten, neu anordnen, senden oder
löschen. Die Einstellung zeigt außerdem das Tastenkürzel, mit dem du für eine Nachricht das andere Verhalten
nutzen kannst, ohne deine Standardeinstellung zu ändern.

Drücke in Codex CLI <kbd>Enter</kbd>, während Codex arbeitet, um die aktuelle
Ausführung zu steuern, oder drücke <kbd>Tab</kbd>, um die Nachricht für die nächste Ausführung einzureihen. Sieh dir für weitere Details die
[interaktiven Tastenkürzel](/codex/developer-commands?surface=cli#cli-interactive-shortcuts)
an.

## Alles zusammenführen

Für ein Projektupdate mit verbundenen Quellen könnte ein vollständiger Prompt etwa
so aussehen:

```text
Prepare a one-page project status update for Monday's leadership meeting. Use
the latest project plan in Drive and relevant decisions and updates from the
project's Slack channel.

Lead with the decisions leadership needs to make and the next steps. Summarize
progress, risks, owners, and due dates. Keep approved dates and budget figures
unchanged. Flag any conflicting or missing information, and don't send or
publish anything.

Before you finish, check that every next step has an owner and due date.

Dieser Prompt umfasst **Ziel**, **Kontext**, **Ausgabe** und **Grenzen** und
fordert anschließend eine abschließende Prüfung an, ohne jeden Schritt einzeln vorzugeben.

## Spracheingabe verwenden

Drücke in der ChatGPT-Desktop-App <kbd>Ctrl+Shift+D</kbd>, während der Editor
sichtbar ist, und beginne zu sprechen. ChatGPT transkribiert das Gesprochene in den Editor,
sodass du den Text prüfen und bearbeiten kannst, bevor du den Prompt sendest.

  
    
  

<a id="threads"></a>
<a id="chats"></a>

## Prompting-Beispiele für Chat

Verwende Chat für Fragen, Ideen, Entwürfe und alltägliche Entscheidungen. Beginne mit dem
gewünschten Ergebnis und füge nur dann Details hinzu, wenn sie die Antwort beeinflussen.

### Ein Thema verstehen

```text
Explain how compound interest works for someone who has never invested.
Use one concrete example and define any financial terms you introduce.

### Texte entwerfen und überarbeiten

```text
Draft a friendly email declining this invitation because I will be traveling.
Keep it under 120 words and leave the door open for a future event.

### Optionen vergleichen

```text
Compare these two phone plans for one person who travels internationally twice
a year. Show the important differences in a table, then recommend one and explain
the tradeoff.

### Einen umsetzbaren Plan erstellen

```text
Plan five weekday dinners that take less than 30 minutes. Avoid peanuts, reuse
ingredients across meals, and finish with one consolidated shopping list.

<a id="prompting-for-work"></a>
<a id="prompting-in-work-mode"></a>

## Prompting für ChatGPT Work

Verwende Chat für kurze Fragen, knappe Überarbeitungen, Brainstorming und einfache
Entwürfe. Verwende ChatGPT Work für Aufgaben, bei denen ChatGPT verschiedene Quellen oder Tools nutzt,
mehrere Schritte ausführt, Änderungen vornimmt oder ein umfangreicheres Ergebnis erstellt.

Beschreibe in ChatGPT Work das gewünschte Ergebnis, stelle das Ausgangsmaterial bereit,
nenne die Zielgruppe und erkläre, wie du die Arbeit überprüfen wirst. Bitte ChatGPT,
das Vorgehen zu planen, die benötigten Informationen zusammenzutragen, Dateien zu erstellen und sie vor dem Abschluss zu prüfen.

<a id="use-work-efficiently"></a>
<a id="use-work-mode-efficiently"></a>

### ChatGPT Work effizient nutzen

ChatGPT Work eignet sich für zeitaufwendige oder wiederkehrende Aufgaben sowie für fertige Dateien, die du
wiederverwenden kannst. Eine Aufgabe kann sich auch dann lohnen, wenn sie mehr Credits verbraucht, sofern sie
Zeit spart, die Qualität verbessert oder dir bei einer wichtigen Entscheidung hilft.

Beginne mit einem Ergebnis, das du überprüfen kannst:

- Beziehe nur relevante Quellen ein und begrenze bei Bedarf den Zeitraum.
- Lege Zielgruppe, Ausgabeformat und gewünschte Länge fest.
- Trenne notwendige Arbeiten von optionalen Verbesserungen oder Feinschliff.
- Bitte um einen Plan, wenn das Vorgehen wichtig ist. Lege fest, dass ChatGPT
deine Genehmigung einholen muss, bevor es Informationen sendet, veröffentlicht oder ändert, auf die sich andere verlassen.
- Schränke die Aufgabe ein oder stoppe sie, wenn ChatGPT mit Arbeiten beginnt, die du nicht mehr brauchst.

Überprüfe das erste Ergebnis, präzisiere die Anweisungen und verwende den Ablauf erneut,
wenn er funktioniert.

### Ausgangsmaterial in fertige Dateien umwandeln

```text
Use the attached quarterly reports to create a leadership brief and a six-slide
presentation.

The audience is the executive team. Lead with the three decisions they need to
make, distinguish reported facts from your analysis, cite each number to its
source file, and check that the brief and slides agree before you finish.

### Eine Entscheidung durch Recherche vorbereiten

```text
Research three customer-support platforms for a 50-person company. Compare
pricing, security, integrations, and migration effort using current sources.
Deliver a recommendation memo with links, assumptions, and the questions we
should answer before signing a contract.

### Eine Markteinführung koordinieren

```text
Create a launch plan for the attached product brief. Include the timeline,
owners, dependencies, risks, announcement draft, customer FAQ, and a checklist
for launch day. Flag any missing decisions before producing the final files.

Verfeinere bei wiederkehrenden Aufgaben zunächst den Prompt in einem normalen Chat. Sobald die Ausgabe
zuverlässig ist, [plane eine Aufgabe in diesem Chat](/de-DE/codex/automations#schedule-a-task-inside-a-chat).
Erstelle stattdessen eine eigenständige geplante Aufgabe, wenn jede geplante Ausführung
einen neuen Chat starten soll.

<a id="use-editor-context"></a>

## Prompting für Codex

Verwende Codex, wenn ChatGPT mit Code, einer Codebasis oder Entwicklungstools arbeiten soll.
Ein hilfreicher Codex-Prompt beschreibt das gewünschte Verhalten, verweist auf relevanten Code oder
die Schritte zum Reproduzieren, hält wichtige Vorgaben fest und erklärt, wie sich die
Änderung überprüfen lässt.

<a id="goal-mode"></a>

Gib bei einer mehrstufigen Aufgabe `/plan` in den Editor der App ein, wenn Codex die Aufgabe vor der Bearbeitung
untersuchen und ein Vorgehen vorschlagen soll. Wenn der [Zielmodus](/de-DE/codex/long-running-work)
verfügbar ist, verwende anschließend `/goal`, um ein dauerhaftes Ziel festzulegen. Sieh dir für die aktuelle Befehlsliste die [Slash-Befehle
der App](/codex/reference/slash-commands)
an.

### So liest du diese Beispiele

Jeder Ablauf umfasst:

- **Wann du ihn einsetzen solltest** und welche Codex-Oberfläche am besten passt (IDE, CLI oder Cloud).
- **Schritte** mit Beispiel-Prompts.
- **Hinweise zum Kontext**: was Codex automatisch als Kontext erhält und was du selbst anhängen solltest.
- **Überprüfung**: wie du die Ausgabe überprüfst.

> **Hinweis:** Die IDE-Erweiterung nimmt deine geöffneten Dateien automatisch in den Kontext auf. Nenne in der CLI Pfade ausdrücklich oder hänge Dateien mit `/mention` und der automatischen Pfadvervollständigung über `@` an.

Codex führt lokale Befehle in einer [Sandbox](/de-DE/codex/sandboxing)
aus, die den Datei- und Netzwerkzugriff einschränkt. Muss eine Aufgabe diese Grenze überschreiten,
hält sich Codex an deine Genehmigungsrichtlinie, bevor es fortfährt.

### Eine Codebasis erklären

Verwende diesen Ablauf, wenn du dich einarbeitest, einen Service übernimmst oder ein Protokoll, ein Datenmodell oder den Ablauf einer Anfrage verstehen möchtest.

#### Ablauf mit der IDE-Erweiterung (am schnellsten für die lokale Analyse)

1. Öffne die relevantesten Dateien.
2. Markiere den Code, den du untersuchen möchtest (optional, aber empfohlen).
3. Gib Codex folgenden Prompt:

   ```text
   Explain how the request flows through the selected code.

   Include:
   - a short summary of the responsibilities of each module involved
   - what data is validated and where
   - one or two "gotchas" to watch for when changing this

Überprüfung:

- Bitte um ein Diagramm oder eine Checkliste mit überprüfbaren Angaben:

```text
Summarize the request flow as a numbered list of steps. Then list the files involved.

#### CLI-Ablauf (geeignet, wenn du ein Transkript und Shell-Befehle brauchst)

1. Starte eine interaktive Sitzung:

   ```bash
   codex

2. Hänge die Dateien an (optional) und gib den Prompt ein:

   ```text
   I need to understand the protocol used by this service. Read @foo.ts @schema.ts and explain the schema and request/response flow. Focus on required vs optional fields and backward compatibility rules.

Hinweise zum Kontext:

- Mit `@` kannst du im Editor Dateipfade aus dem Workspace einfügen oder mit `/mention` eine bestimmte Datei anhängen.

### Einen Fehler beheben

Verwende diesen Ablauf, wenn du einen Fehler lokal reproduzieren kannst.

#### CLI-Ablauf (kurzer Zyklus aus Reproduktion und Überprüfung)

1. Starte Codex im Stammverzeichnis des Repositorys:

   ```bash
   codex

2. Beschreibe Codex die Schritte zum Reproduzieren und nenne die Dateien, in denen du den Fehler vermutest:

   ```text
   Bug: Clicking "Save" on the settings screen sometimes shows "Saved" but doesn't persist the change.

   Repro:
   1) Start the app: npm run dev
   2) Go to /settings
   3) Toggle "Enable alerts"
   4) Click Save
   5) Refresh the page: the toggle resets

   Constraints:
   - Do not change the API shape.
   - Keep the fix minimal and add a regression test if feasible.

   Start by reproducing the bug locally, then propose a patch and run checks.

Hinweise zum Kontext:

- Von dir bereitgestellt: die Schritte zum Reproduzieren und die Vorgaben (sie sind wichtiger als eine allgemeine Beschreibung).
- Von Codex bereitgestellt: Befehlsausgaben, gefundene Aufrufstellen und etwaige dabei ausgelöste Stacktraces.

Überprüfung:

- Codex sollte die Schritte zum Reproduzieren nach der Fehlerbehebung erneut ausführen.
- Wenn du eine standardmäßige Prüfpipeline hast, bitte Codex, sie auszuführen:

```text
After the fix, run lint + the smallest relevant test suite. Report the commands and results.

#### Ablauf mit der IDE-Erweiterung

1. Öffne die Datei, in der du den Fehler vermutest, sowie die unmittelbar aufrufende Stelle.
2. Gib Codex folgenden Prompt:

   ```text
   Find the bug causing "Saved" to show without persisting changes. After proposing the fix, tell me how to verify it in the UI.

### Einen Test schreiben

Verwende diesen Ablauf, wenn du den genauen Testumfang festlegen möchtest.

#### Ablauf mit der IDE-Erweiterung (auf Basis einer Auswahl)

1. Öffne die Datei mit der Funktion.
2. Markiere die Zeilen, in denen die Funktion definiert ist. Wähle in der Befehlspalette „Add to Codex Thread“ aus, um diese Zeilen zum Kontext hinzuzufügen.
3. Gib Codex folgenden Prompt:

   ```text
   Write a unit test for this function. Follow conventions used in other tests.

Hinweise zum Kontext:

- Vom Befehl „Add to Codex Thread“ bereitgestellt: die ausgewählten Zeilen (das ist der durch Zeilennummern festgelegte Bereich) sowie die geöffneten Dateien.

#### CLI-Ablauf (Pfad und Zeilenbereich im Prompt beschrieben)

1. Starte Codex:

   ```bash
   codex

2. Verwende einen Funktionsnamen im Prompt:

   ```text
   Add a test for the invert_list function in @transform.ts. Cover the happy path plus edge cases.

### Prototyp anhand eines Screenshots erstellen

Nutze diesen Ablauf, wenn du aus einem Designentwurf, Screenshot oder einer UI-Vorlage einen funktionsfähigen Prototyp erstellen möchtest.

#### CLI-Ablauf (Bild + Prompt)

1. Speichere deinen Screenshot lokal (zum Beispiel `./specs/ui.png`).
2. Starte Codex:

   ```bash
   codex

3. Ziehe die Bilddatei in das Terminal, um sie an den Prompt anzuhängen.

4. Gib anschließend Rahmenbedingungen und Struktur vor:

   ```text
   Create a new dashboard based on this image.

   Constraints:
   - Use react, vite, and tailwind. Write the code in typescript.
   - Match spacing, typography, and layout as closely as possible.

   Outputs:
   - A new route/page that renders the UI
   - Any small components needed
   - README.md with instructions to run it locally

Hinweise zum Kontext:

- Das Bild gibt die visuellen Anforderungen vor, die Vorgaben für die Implementierung musst du jedoch selbst festlegen (Framework, Routing, Komponentenstil).
- Beschreibe zusätzlich in Textform Verhalten, das im Bild nicht zu sehen ist, etwa Hover-Zustände, Validierungsregeln oder Tastaturinteraktionen.

Überprüfung:

- Bitte Codex, den Entwicklungsserver zu starten (sofern zulässig) und dir genau zu sagen, wo du nachsehen sollst:

```text
Start the dev server and tell me the local URL/route to view the prototype.

#### Ablauf für die IDE-Erweiterung (Bild + vorhandene Dateien)

1. Hänge das Bild im Codex-Chat an (per Drag-and-drop oder durch Einfügen).
2. Gib Codex folgenden Prompt:

   ```text
   Create a new settings page. Use the attached screenshot as the target UI.
   Follow design and visual patterns from other files in this project.

### UI mit Live-Updates weiterentwickeln

Nutze diesen Ablauf, wenn du in schnellen Zyklen nach dem Muster „Entwerfen → anpassen → neu laden → anpassen“ arbeiten möchtest, während Codex den Code bearbeitet.

#### CLI-Ablauf (Vite starten und anschließend mit kurzen Prompts iterieren)

1. Starte Codex:

   ```bash
   codex

2. Starte den Entwicklungsserver in einem separaten Terminalfenster:

   ```bash
   npm run dev

3. Fordere Codex auf, Änderungen vorzunehmen:

   ```text
   Propose 2-3 styling improvements for the landing page.

4. Wähle eine Richtung und entwickle sie mit kurzen, konkreten Prompts weiter:

   ```text
   Go with option 2.

   Change only the header:
   - make the typography more editorial
   - increase whitespace
   - ensure it still looks good on mobile

5. Wiederhole den Vorgang mit gezielten Anfragen:

   ```text
   Next iteration: reduce visual noise.
   Keep the layout, but simplify colors and remove any redundant borders.

Überprüfung:

- Prüfe die Änderungen im Browser, während Codex den Code aktualisiert.
- Erstelle Commits für Änderungen, die dir gefallen, und mache unerwünschte Änderungen rückgängig.
- Wenn du eine Änderung rückgängig machst oder anpasst, teile das Codex mit, damit Codex deine Änderung beim nächsten Prompt nicht überschreibt.

### Refactoring an die Cloud delegieren

Nutze diesen Ablauf, wenn du anhand des lokalen Kontexts einen Ansatz entwickeln und die langwierige Implementierung anschließend an einen parallel laufenden Cloud-Chat delegieren möchtest.

#### Lokale Planung (IDE)

1. Stelle sicher, dass deine aktuelle Arbeit in einem Commit gesichert oder zumindest per Stash zwischengespeichert ist, damit du die Änderungen sauber vergleichen kannst.
2. Bitte Codex, einen Refactoring-Plan zu erstellen. Wenn der Skill `$plan` verfügbar ist, rufe ihn ausdrücklich auf:

   ```text
   $plan

   We need to refactor the auth subsystem to:
   - split responsibilities (token parsing vs session loading vs permissions)
   - reduce circular imports
   - improve testability

   Constraints:
   - No user-visible behavior changes
   - Keep public APIs stable
   - Include a step-by-step migration plan

3. Prüfe den Plan und stimme Änderungen mit Codex ab:

   ```text
   Revise the plan to:
   - specify exactly which files move in each milestone
   - include a rollback strategy

Hinweise zum Kontext:

- Die Planung gelingt am besten, wenn Codex den aktuellen Code lokal untersuchen kann (Einstiegspunkte, Modulgrenzen, Hinweise auf den Abhängigkeitsgraphen).

#### Delegation an die Cloud (IDE → Cloud)

1. Richte, falls noch nicht geschehen, eine [Codex-Cloud-Umgebung](/de-DE/codex/environments/cloud-environment) ein.
2. Klicke auf das Cloud-Symbol unter dem Prompt-Editor und wähle deine Cloud-Umgebung aus.
3. Wenn du den nächsten Prompt eingibst, erstellt Codex einen neuen Chat in der Cloud und übernimmt den bisherigen Chat-Kontext (einschließlich des Plans und lokaler Änderungen am Quellcode).

   ```text
   Implement Milestone 1 from the plan.

4. Prüfe den Cloud-Diff und nimm bei Bedarf weitere Anpassungen vor.

5. Erstelle einen PR direkt in der Cloud oder rufe die Änderungen lokal ab, um sie zu testen und die Arbeit abzuschließen.

6. Bearbeite weitere Meilensteine des Plans schrittweise.

An die Cloud delegierte Aufgaben werden in isolierten Umgebungen ausgeführt. Der Internetzugang ist
während der Agentenphase deaktiviert, sofern du ihn nicht für die Umgebung aktivierst. Weitere Informationen
zum [Internetzugang in der Cloud](/de-DE/codex/cloud/internet-access).

### Code lokal überprüfen

Nutze diesen Ablauf, wenn du deinen Code vor einem Commit oder der Erstellung eines PR noch einmal prüfen lassen möchtest.

#### CLI-Ablauf (dein Arbeitsverzeichnis überprüfen)

1. Starte Codex:

   ```bash
   codex

2. Führe den Review-Befehl aus:

   ```text
   /review

3. Optional: Gib eigene Prüfschwerpunkte vor:

   ```text
   /review Focus on edge cases and security issues

Überprüfung:

- Nimm anhand des Review-Feedbacks Korrekturen vor und führe anschließend `/review` erneut aus, um sicherzustellen, dass die Probleme behoben sind.

### Einen Pull Request auf GitHub überprüfen

Nutze diesen Ablauf, wenn du Review-Feedback erhalten möchtest, ohne den Branch lokal abzurufen.

Bevor du diese Funktion nutzen kannst, aktiviere Codex **Code Review** für dein Repository. Weitere Informationen findest du unter [Code Review](/de-DE/codex/third-party/github).

#### GitHub-Ablauf (über Kommentare gesteuert)

1. Öffne den Pull Request auf GitHub.
2. Hinterlasse einen Kommentar, in dem du Codex markierst und konkrete Prüfschwerpunkte angibst:

   ```text
   @codex review

3. Optional: Gib genauere Anweisungen.

   ```text
   @codex review for security vulnerabilities and security concerns

### Dokumentation aktualisieren

Nutze diesen Ablauf, wenn du eine fachlich korrekte und verständliche Änderung an der Dokumentation benötigst.

#### IDE- oder CLI-Ablauf (lokale Änderungen + lokale Validierung)

1. Ermittle die zu ändernden Dokumentationsdateien und öffne sie (IDE) oder referenziere sie mit `@` (IDE oder CLI).
2. Gib Codex einen Prompt mit dem gewünschten Umfang und den Anforderungen an die Validierung:

   ```text
   Update the "advanced features" documentation to provide authentication troubleshooting guidance. Verify that all links are valid.

3. Nachdem Codex einen Entwurf der Änderungen erstellt hat, überprüfe die Dokumentation und passe sie bei Bedarf weiter an.

Überprüfung:

- Lies die gerenderte Seite.

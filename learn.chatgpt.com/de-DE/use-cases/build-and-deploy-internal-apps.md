<!-- source: https://learn.chatgpt.com/de-DE/use-cases/build-and-deploy-internal-apps -->

## Mit einer einzigen Aufgabe entwickeln und bereitstellen

Sites ist ein vollständig verwalteter Hosting-Dienst in ChatGPT. Bitte ChatGPT, eine App zu erstellen. ChatGPT kann daraufhin das Projekt entwickeln, zum Testen ausführen, bereitstellen und eine URL zurückgeben, die du teilen kannst.

Sites befindet sich für unterstützte kostenpflichtige Tarife in der öffentlichen Betaphase. Zum Start ist Sites weder in Free noch in Go verfügbar, ebenso wenig im EWR, in der Schweiz oder im Vereinigten Königreich. Auch die schrittweise Einführung und Workspace-Einstellungen können den Zugriff beeinflussen.

Das Spektrum reicht von statischen Websites bis zu Full-Stack-Web-Apps in JavaScript oder TypeScript. Daher eignet sich Sites gut für klar umrissene interne Tools: Onboarding-Dashboards, Schulungsportale, durchsuchbare Ressourcenbibliotheken, schlanke Workflow-Apps und Berichtsansichten.

Informationen zu Setup, Speicher, Bereitstellung und Zugriff findest du in der [Sites-Dokumentation](/de-DE/codex/sites).

Beginne mit einem einzigen nützlichen Workflow. Eine klar definierte erste Version lässt sich leichter überprüfen, bereitstellen und verbessern als eine weit gefasste Anfrage, mit der ein komplettes internes System nachgebildet werden soll.

## Was dich erwartet

Hier siehst du ein fiktives Beispiel mit einem angehängten Launch-Briefing und fünf Beispielanfragen. Im ersten Durchlauf wird ein klar umrissener Tracker für Anfragen erstellt und geprüft; eine Folgeanfrage ergänzt einen Filter nach zuständiger Person und macht überfällige Anfragen leichter erkennbar.

<div data-use-case-export-only>

Der Tracker für Launch-Anfragen enthält zunächst **fünf Beispielanfragen**, darunter eine blockierte Anfrage, zwei Anfragen im Review und einen überfälligen Eintrag. Das Team kann die Anfragen anhand von Launch und Status durchsehen, blockierte Anfragen filtern, eine Anfrage hinzufügen und ihren Status aktualisieren. Der Hauptablauf und der gespeicherte Zustand wurden in Desktop- und Mobilansichten geprüft.

Nach einer Folgeanfrage enthält der Tracker einen Filter nach zuständiger Person und hebt überfällige Anfragen hervor; **blockierte Anfragen bleiben oben, und eine Anfrage kann ohne zuständige Person nicht als bereit markiert werden**. Die Vorschau bleibt privat; keine Site wurde veröffentlicht und der Zugriff wurde nicht geändert.

</div>

## ChatGPT den Workflow-Kontext geben

Erkläre ChatGPT, für wen die App gedacht ist, was die Zielgruppe damit tun soll, welches Ausgangsmaterial ChatGPT prüfen soll und was zwischen Sitzungen erhalten bleiben soll. Lege den vorgesehenen Freigabekreis eindeutig fest und bitte ChatGPT, den Hauptablauf vor der Bereitstellung zu testen.

Nutze [Plug-ins](/de-DE/codex/plugins), um Daten aus verbundenen internen Quellen abzurufen oder zu aktualisieren. Starte eine Sites-Aufgabe, die verbundene Apps oder Cloud-Dateien nutzt, in Work im Web oder auf dem Desktop in Work beziehungsweise Codex. Nutze für eine lokale Datei die Desktop-App, für eine Website, auf der du angemeldet bist, den integrierten Browser oder für eine bestehende Chrome-Sitzung die Codex Chrome-Erweiterung.

  Wenn du Daten in Echtzeit abrufen musst, kannst du ein Drittanbieter-Tool mithilfe eines
  API-Schlüssels anbinden, der in den Einstellungen der Site konfiguriert ist. Speichere geheime Werte weder in Prompts
  noch in Dateien. Wenn du Plug-in-Verbindungen nutzen möchtest, kannst du [Arbeit aus
  der aktuellen Aufgabe heraus planen](/de-DE/codex/automations#schedule-work-from-a-task), um Daten
  mit Plug-ins nach einem festen Zeitplan abzurufen, die App zu aktualisieren und eine Version zur Prüfung zu speichern.
  Stelle die geprüfte Version erst nach der Genehmigung bereit.

## Speicher für die App auswählen

Viele interne Apps müssen Daten dauerhaft speichern. Sites unterstützt dafür zwei Speicherarten:

- Verwende D1, eine SQLite-kompatible Datenbank, für strukturierte Daten wie Checklistenstatus, Lesezeichen, Filter, Anmerkungen, Konfigurationsdaten und Dateimetadaten.
- Verwende den R2-Objektspeicher für die Binärdaten von Dateien, die dauerhaft gespeichert werden sollen, etwa für hochgeladene Dokumente, Bilder oder andere Assets.

Speichere strukturierte Metadaten in D1 und größere Dateiobjekte in R2. Eine Ressourcenseite ohne Schreibzugriff oder eine kleine statische Website benötigt möglicherweise keines von beiden.

Sites unterstützt keine Daten- oder Inferenzresidenz. Nutze Sites nicht, um geschützte Gesundheitsdaten oder Zahlungskartendaten zu verarbeiten oder Finanztransaktionen zu ermöglichen. Prüfe die [Daten- und Nutzungsbeschränkungen für Sites](https://help.openai.com/en/articles/20001339-creating-and-managing-chatgpt-sites), bevor du vertrauliche Informationen speicherst.

## Projekte verwalten und freigeben

Du kannst festlegen, wer deine bereitgestellten Projekte aufrufen darf.

Halte ein neues Projekt privat, während du seine Inhalte, den Umgang mit Daten und die vorgesehene Zielgruppe prüfst.

Je nach deinen Konto- und Workspace-Einstellungen kannst du es für folgende Personen freigeben:

- Personen, die du einlädst.
- Alle in deinem Workspace.
- Alle im Internet.

Durch die Freigabe können andere Personen das Projekt aufrufen, aber nicht bearbeiten. Um den Zugriff zu ändern, öffne [Sites in ChatGPT](https://chatgpt.com/sites) oder bitte ChatGPT direkt darum:

Die öffentliche Freigabe eignet sich auch für einen kompakten Veranstaltungsleitfaden, eine Ressourcenseite für einen Verein oder eine andere Site für Personen außerhalb eines Workspaces. In Unternehmens-Workspaces ist die öffentliche Veröffentlichung standardmäßig deaktiviert und muss von einer Person mit Administratorrechten aktiviert werden. Halte interne Daten auch dann privat, wenn ein öffentlicher Link verfügbar ist.

## Beispiele

Der [Sites-Showcase](/showcase/sites) enthält Beispiel-Sites mit vollständigen Prompts.

{/* vale Vale.Spelling = NO */}
{/* vale Vale.Terms = NO */}

- **[Onboarding Hub](/showcase/onboarding-hub)** bündelt eine Checkliste für die erste Woche, Ressourcen, Notizen und hochgeladene Dokumente. Die App verwendet D1 für individuelle Statusdaten und Dateimetadaten sowie R2 für die Binärdaten hochgeladener Dateien.
- **[Enablement Hub](/showcase/enablement-hub)** bietet eine durchsuchbare Schulungsbibliothek mit Filtern und gespeicherten Lesezeichen, die in D1 hinterlegt sind.
- **[Pulse Dashboard](/showcase/pulse-dashboard)** zeigt Kennzahlen, Trends und Details zur Datenherkunft und verwendet D1 für die Konfiguration und zwischengespeicherte Snapshots.
- **[Sparkboard](/showcase/idea-intake)** verwandelt die Ideenerfassung unter Mitarbeitenden in einen Workflow mit authentifizierten Einreichungen, Abstimmungen, Kommentaren, Statusübersichten und Ranglisten der Mitwirkenden.
- **[Launch Cal](/showcase/launch-cal)** ordnet bevorstehende Produkt-Launches in einem Monatskalender mit Filtern, Risikosignalen, Checklisten und Verweisen auf verbundene Quellen.
- **[Event Planning Hub](/showcase/event-planning-hub)** bündelt Veranstaltungsanfragen, Genehmigungen, Vorlagen, Meilensteine, den Status der Richtlinienkonformität und verbundene Planungsressourcen.

{/* vale Vale.Terms = YES */}
{/* vale Vale.Spelling = YES */}

Nutze diese Beispiele als Ausgangspunkte und richte den Prompt anschließend gezielt auf den Workflow und das Ausgangsmaterial deines Teams aus.

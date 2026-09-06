<!-- source: https://learn.chatgpt.com/de-DE/use-cases/automation-bug-triage -->

## So gehst du vor

Lass Codex die Quellen prüfen, in denen Bugs bereits auftauchen: Sentry-Warnmeldungen, Linear-Issues, GitHub-Issues, PR-Checks, Deployment-Protokolle, Supporttickets und Slack-Threads. Beginne mit einem manuellen Durchlauf, passe den Bericht im Chat an und führe ihn dann nach Zeitplan aus.

Verwende für den gesamten Triage-Zyklus einen einzigen Codex-Chat:

1. Führe bei Bedarf einen Triage-Durchlauf aus und lass dir eine vorläufige Liste erstellen.
2. Prüfe die Liste und gib im selben Chat Feedback.
3. Plane aus diesem Chat heraus eine Aufgabe für die Triage.
4. Optional: Bitte Codex, Linear-Issues, Slack-Aktualisierungen, GitHub-Kommentare oder Übergabenotizen zu entwerfen, wenn du sicher bist, dass der Bericht stimmt.

Installiere zunächst die [Plug-ins](/de-DE/codex/plugins), die Codex benötigt, etwa Sentry, Slack, Linear oder GitHub. Ersetze im Starter-Prompt die Plug-in-Liste in eckigen Klammern durch echte Plug-in-Chips, die mit `@` beginnen. Ersetze anschließend jede in eckigen Klammern angegebene Quelle durch den genauen Ort, der durchsucht werden soll: ein Sentry-Projekt oder eine Warnmeldungs-URL, einen Slack-Kanal oder -Thread, ein Linear-Team, eine Ansicht oder Abfrage, ein GitHub-Repository, eine Issue-Abfrage oder einen PR-Check, einen Deployment-Link, eine Protokolldatei, eine Support-Warteschlange oder ein Dashboard.

## Phase 1: Triage-Durchlauf ausführen

Starte Codex in dem Repository, auf das sich die Bugs beziehen, wenn lokaler Kontext hilfreich ist: Tests, Repository-Tools, Build-Checks oder CI-Fehler. Du kannst den Durchlauf auch aus jedem beliebigen Repository heraus starten, wenn deine Bug-Quellen über Plug-ins, Konnektoren, MCP-Server, Links, Exporte, eingefügte Protokolle oder Anhänge verfügbar sind.

Führe zuerst den oben stehenden Starter-Prompt aus. Behalte nur die Plug-ins und Quellen bei, die Teil deines Durchlaufs sind.

Ein ausgefüllter Prompt kann beispielsweise die Plug-ins sowie die genauen Warteschlangen, Kanäle oder Repositories nennen, die du in den Durchlauf aufnehmen möchtest.

<div class="not-prose mb-12 rounded-xl bg-[url('/images/codex/codex-wallpaper-1.webp')] bg-cover bg-center p-4 md:p-8">
  
</div>

## Phase 2: Den Bericht aussagekräftig machen

Bevor du den Ablauf automatisierst, stelle sicher, dass der Bericht so nützlich ist, dass es sich lohnt, ihn täglich zu lesen.

Ein hilfreicher erster Durchlauf umfasst:

- Relevante Bugs, von P0 bis P3 sortiert.
- Doppelte Meldungen werden unter einem Bug zusammengefasst.
- Zu jedem Bug gibt es verlinkte Belege oder kurze Quellenangaben.
- Beobachtete Fakten und Vermutungen sind klar voneinander getrennt.
- Für jeden Bug gibt es eine kurze Empfehlung für den nächsten Schritt.

Passe den Bericht im selben Chat an, bevor du seine regelmäßige Ausführung planst. Du kannst Codex bitten:

- Vor der Priorisierung der Liste eine weitere Quelle zu prüfen.
- Wenig aussagekräftige Warnmeldungen wegzulassen, die dem Team bereits bekannt sind.
- Nur Bugs der Prioritäten P0 und P1 zurückzugeben.
- Slack-Meldungen, Sentry-Warnmeldungen und GitHub-Fehler zusammenzuführen, wenn sie auf denselben Bug hindeuten.
- Für jeden Bug nur den besten Link anzuzeigen.
- Genügend Belege hinzuzufügen, damit andere das Problem reproduzieren oder an die zuständige Stelle weiterleiten können.

## Phase 3: Automatisieren

Sobald der Bericht aus dem manuellen Durchlauf nützlich ist, bleib im selben Chat und [plane daraus eine Aufgabe für die Triage](/de-DE/codex/automations#schedule-a-task-inside-a-chat). Codex kann auf Grundlage deiner Anpassungen im Chat den Prompt für die regelmäßige Ausführung formulieren.

**Triage als Aufgabe planen**

## Phase 4: Folgeschritte weiterleiten

Sobald der geplante Bericht brauchbar ist, lege fest, wo die daraus entstehenden Aufgaben bearbeitet werden sollen. Codex kann ein Slack-Update für einen Teamkanal entwerfen, Linear-Issues für die Bugs erstellen, die du nachverfolgen möchtest, GitHub-Kommentare zu einem PR mit fehlgeschlagenen Checks verfassen oder eine Übergabe für die Rufbereitschaft vorbereiten.

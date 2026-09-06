<!-- source: https://learn.chatgpt.com/de-DE/use-cases/slack-action-triage -->

## Versteckte Aufgaben in Slack finden

Eine Anfrage beginnt oft in Slack, doch der vollständige Kontext liegt meist woanders. Jemand aus deinem Team bittet dich vielleicht in einer DM um eine Antwort, präzisiert die eigentliche Aufgabe in einem Thread, verlinkt ein Dokument in einem Channel und klärt das Anliegen später, ohne dich erneut zu erwähnen.

Nutze diesen Workflow, damit ChatGPT den Slack-Kontext liest, prüft, ob die Anfrage noch offen ist, und nur die wenigen Punkte zurückgibt, die wirklich deine Aufmerksamkeit erfordern. Das Ziel ist eine priorisierte Aufgabenliste: Welche Punkte erfordern eine Antwort, eine Entscheidung, die Kontaktaufnahme mit einer Person, eine Aktualisierung der Dokumentation oder eine Übergabe?

## Triage durchführen

1. Gib ChatGPT einen Zeitraum, einen Arbeitsbereich, eine Person, einen Channel oder ein Thema vor.
2. Bitte ChatGPT, DMs, Gruppen-DMs, Erwähnungen in Channels und relevante Antworten in Threads zu durchsuchen.
3. Bitte ChatGPT, die neuesten Antworten am Ende des Threads zu lesen, bevor es einen Punkt als ungelöst einstuft.
4. Bitte um eine nach Dringlichkeit und Auswirkung sortierte Aufgabenliste.
5. Bitte ChatGPT, einen Entwurf für die Antwort, Übergabe oder Folgeaufgabe zu erstellen.

Nachdem du diesen Ablauf ausprobiert und an deine Bedürfnisse angepasst hast, kannst du [direkt aus dem Chat eine Aufgabe für diesen Ablauf planen](/de-DE/codex/automations#schedule-a-task-inside-a-chat), indem du ChatGPT bittest, ihn nach einem Zeitplan auszuführen.

## Das passende Ergebnis anfordern

Ein hilfreiches Triage-Ergebnis sollte für jeden Punkt erklären, warum er noch offen ist. Außerdem sollte es alte Anfragen auslassen, die später im Thread beantwortet wurden.

Das Ergebnis sollte ungefähr so aussehen:

  <p>
    <strong>Wichtigste Aufgabe:</strong> Priya bittet um konkrete Beispiele aus der Kundschaft
    und nicht nur um weitere Ideen.
  </p>
  <p>
    <strong>Warum das wichtig ist:</strong> Das Team braucht für das Launch-Update konkrete Personen,
    die es diese Woche kontaktieren kann.
  </p>
  <p>
    <strong>Beleg:</strong> In der ursprünglichen Channel-Nachricht wurde nach Anwendungsfällen gefragt,
    später heißt es im Thread jedoch: „Schick mir bitte eine DM, wenn du Kontakte hast.“
  </p>
  <p>
    <strong>Nächster Schritt:</strong> Nenne in deiner Antwort zwei konkrete Kontakte oder biete dich selbst
    als Beispiel an, wenn das hilfreicher ist.
  </p>

Ein gutes Ergebnis macht die Unterschiede deutlich: Eine Idee ist etwas anderes als ein konkreter Kontakt, eine offene Anfrage etwas anderes als eine reine Information, und eine bereits von dir beantwortete Anfrage gehört nicht mehr auf die Aufgabenliste.

Wenn du zu viele irrelevante oder zu wenige umsetzbare Punkte erhältst, passe den Prompt an. Nenne bei Bedarf auch bestimmte Slack-Channels, auf die ChatGPT besonders achten soll.

## Die Folgenachricht entwerfen

Wenn die Aufgabenliste passt, führe den nächsten Schritt im selben Chat aus. Bitte ChatGPT, auf Grundlage der bereits gesammelten Belege eine Antwort oder Übergabe zu entwerfen:

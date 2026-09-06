<!-- source: https://learn.chatgpt.com/de-DE/use-cases/manage-your-inbox -->

## Bevor du beginnst

Diesen Ablauf kannst du in ChatGPT Work im Browser oder in der Desktop-App ausführen. Bevor du beginnst:

- **Verbinde dein E-Mail-Konto.** Installiere das [Plug-in für Gmail oder Outlook Email](/de-DE/docs/plugins). Du kannst außerdem Slack, Google Drive und deinen Kalender verbinden, damit ChatGPT beim Entwerfen von Antworten mehr Kontext erhält.
- **Lege fest, wo geplante Prüfungen ausgeführt werden.** Beginne im Browser, wenn die Prüfungen weiterlaufen sollen, während dein Laptop ausgeschaltet ist. Wenn du die Desktop-App nutzt, lass deinen Computer eingeschaltet und die ChatGPT-Desktop-App weiterlaufen. Sprachchats unterstützen keine [geplanten Aufgaben](/de-DE/docs/automations). Richte sie daher stattdessen im Chat ein oder verwalte sie dort.

## Was dich erwartet

ChatGPT prüft aktuelle E-Mails, erkennt Nachrichten, die deine Aufmerksamkeit erfordern, schlägt eine Bereinigung vor und bereitet Antworten vor, ohne sie zu senden. Sobald du die Bereinigung genehmigst, kann ChatGPT diese Änderungen auf ältere, noch unbearbeitete E-Mails anwenden. So kann das Gespräch aussehen:

<div data-use-case-export-only>

Ich habe deinen verbundenen beruflichen Posteingang geprüft, mit Schwerpunkt auf Produkteinführungen, Dokumentation und Produktionsarbeit. Er enthält **116 Nachrichten, davon 96 ungelesen**; die meisten ungelesenen E-Mails betreffen Projektaktivitäten, Kalenderaktualisierungen, Benachrichtigungen zu freigegebenen Dateien und Newsletter.

### Was deine Aufmerksamkeit erfordert

- **Aufnahmevorbereitung:** Sende vor dem morgigen Termin die angeforderten Demo-Themen, eine Kurzbiografie und ein Foto.
- **Dokumentationsprüfung:** Berücksichtige das Feedback zur korrekten Produktdarstellung, bevor die Arbeit an der Anleitung fortgesetzt wird.
- **Fehlgeschlagenes Preview-Deployment:** Untersuche den fehlgeschlagenen Build, bevor du dich auf die aktuellen Änderungen verlässt.
- **Aufgabe zu Zusatzleistungen:** Schließe die ausstehende Änderung der Zusatzleistungen ab.
- **Anmeldewarnung:** Prüfe, ob die letzte Anmeldung von dir stammt. Falls nicht, folge den Anweisungen in der Warnung.

### Bereinigung

Ich würde routinemäßige Projekt-, Kalender- und Dokumentbenachrichtigungen mit den Labels `Project activity`, `Calendar` und `Docs` versehen und archivieren; archivierte E-Mails bleiben durchsuchbar. Direkte Anfragen, laufende Reviews, fehlgeschlagene Builds, Sicherheitswarnungen und alles Ungeklärte würden sichtbar bleiben. Newsletter und andere wiederkehrende Abonnements sollten gesondert geprüft werden.

### Eine Antwort an die für die Aufnahme zuständige Person

Die für die Aufnahme zuständige Person wartet auf Demo-Themen, eine Kurzbiografie und ein Foto. Ich habe den aktuellen Stand der Terminplanung geprüft und eine Antwort in deinem Stil entworfen:

> Ich freue mich darauf. Ich plane, die drei besprochenen Arbeitsabläufe zu zeigen, und schicke die Kurzbiografie und das Foto heute. Die aktualisierte Kalendereinladung habe ich gesehen und richte mich nach der neuen Uhrzeit.

Künftig prüfe ich **montags bis freitags um 8 und 16 Uhr**. Ich hebe neue oder geänderte E-Mails hervor, die deine Aufmerksamkeit erfordern, prüfe bei Bedarf verbundene Quellen wie Chats, Dokumente oder deinen Kalender und bereite Antworten in deinem Stil vor. Du kannst mir jederzeit neue Anweisungen geben, indem du hier antwortest.

### Was soll ich tun?

1. **Die Bereinigung anwenden?** Ja / Nein. Routinemäßige Nachrichten werden mit Labels versehen und archiviert, nicht gelöscht.
2. **Die Antwort als Entwurf speichern?** Ja / Nein.
3. **Den vorgeschlagenen Zeitplan und die Prioritäten beibehalten?** Ja / Nein.

Antworte mit „1 ja, 2 ja, 3 nein“ und gib gewünschte Änderungen an.

</div>

**Warnung:** Das Gmail-Plug-in kann E-Mails in den Papierkorb verschieben, wenn du ausdrücklich darum bittest. Prüfe zuerst die vorgeschlagenen Gruppen und einige Beispielnachrichten. Archiviere alles, bei dem du unsicher bist, statt es zu löschen. Die verfügbaren Aktionen können je nach E-Mail-Plug-in und Workspace-Einstellungen variieren.

## So funktioniert es

Ein E-Mail-Ablauf besteht aus mehreren Teilen:

- **Kontext aus verbundenen Quellen:** Plug-ins ermöglichen ChatGPT, deine E-Mails zu lesen und andere verbundene Tools zu prüfen, wenn für eine Antwort mehr Kontext nötig ist. In Slack findest du möglicherweise die letzte Unterhaltung oder Entscheidung, in Google Drive relevante Dateien oder Projektunterlagen. Dein Kalender kann bei der Klärung von Terminen oder Besprechungen helfen.
- **Prioritäten:** Du kannst ChatGPT mitteilen, welche Personen, Anfragen, Warnungen und wiederkehrenden Nachrichten priorisiert oder ignoriert werden sollen. Künftige Prüfungen können diese Anweisungen berücksichtigen.
- **Genehmigungspflichtige Aktionen:** ChatGPT schlägt eine Bereinigung vor und entwirft Antworten, führt aber erst nach deiner Genehmigung Aktionen aus.
- **Geplante Aufgaben:** Statt auf deine Rückkehr und eine erneute Aufforderung zu warten, kann ChatGPT innerhalb derselben Aufgabe zu festgelegten Zeiten nach neuen Nachrichten suchen.

## Erstelle deinen eigenen E-Mail-Ablauf

Wenn du bereits weißt, was du möchtest, kannst du konkreter formulieren. Ein Prompt für **berufliche E-Mails**
könnte laufende Unterhaltungen, Anfragen, Genehmigungen und den
Projektkontext hervorheben:

Ein Prompt für **private E-Mails** könnte stattdessen Personen aus deinem Umfeld, Rechnungen,
Pakete, Reisen, Termine und Kontowarnungen in den Mittelpunkt stellen:

Beide Beispiele folgen derselben Grundstruktur: was geprüft werden soll, was wichtig ist, was zu tun ist, wann es zu tun ist und wofür eine Genehmigung erforderlich ist.

## Weitere Möglichkeiten

Sobald der grundlegende Ablauf läuft, kannst du ihn verfeinern oder ChatGPT bitten, weitere nützliche E-Mail-Aufgaben zu übernehmen.

**Immer den passenden Kontext prüfen**

**Ein regelmäßiges Update entwerfen**

**Bei unbeantworteten E-Mails nachfassen**

**Format ändern**

**Festlegen, was wichtig ist**

**Antwortentwürfe anpassen**

**Prüfzeiten ändern**

Lass Bereinigungs- und Antwortaktionen erst nach deiner Genehmigung ausführen, bis du den Regeln vertraust.

Gmail- und Outlook-Aktionen sowie geplante Aufgaben hängen von deinem Tarif und den Workspace-Einstellungen ab.

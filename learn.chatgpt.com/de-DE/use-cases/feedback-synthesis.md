<!-- source: https://learn.chatgpt.com/de-DE/use-cases/feedback-synthesis -->

## Bevor du beginnst

Produktfeedback kann in Slack, Umfrageexporten, Issue-Trackern, Supportunterlagen oder Forschungsnotizen vorliegen. Übermittle ChatGPT Work die Quellen sowie den zu prüfenden Produktbereich und Zeitraum. ChatGPT Work kann wiederkehrende Probleme in einer Tabelle oder einem Dokument gruppieren. So kann das Team sie prüfen, bevor es über die nächsten Schritte entscheidet.

Starte diesen Workflow in Work, entweder im Web oder auf dem Desktop, und nutze dabei verbundene Apps und Cloud-Dateien. Wenn die Quelle auf deinem Computer gespeichert ist, hänge zuerst einen lokalen Export an oder verwende die Desktop-App.

## Was dich erwartet

Das folgende Beispiel nutzt einen Umfrageexport, Supportunterlagen, einen Feedback-Thread und Forschungsnotizen für eine Warteschlange zur Prüfung von Anfragen. Im ersten Durchlauf werden wiederkehrende Probleme gruppiert. Anschließend wird ein zu breit gefasstes Thema in zwei klarere Entscheidungen aufgeteilt.

<div data-use-case-export-only>

Im ersten Durchlauf wurden in einer Umfrage, in Supportunterlagen, in einem Feedback-Thread und in Forschungsnotizen drei wiederkehrende Probleme gefunden:

- **Konflikte sind in der Warteschlange nicht sichtbar:** acht Nennungen in vier Quellen. Zeige den Konfliktstatus in der Liste an und unterscheide `Ready` von `Needs attention`.
- **Eine Sammelgenehmigung kann blockierte Anfragen umfassen:** vier Nennungen in vier Quellen. Überspringe blockierte Anfragen standardmäßig oder zeige vor der Genehmigung eine Warnung an.
- **Prüfende verlieren ihre Position und können Vorgänge nicht gezielt herausfiltern:** zehn Nennungen in vier Quellen. Behalte Suche und Filter bei und biete eine Ansicht für `Needs attention` an.

Nach einem weiteren Schritt zur Aufteilung des letzten Themas unterscheidet die Tabelle zwischen **dem Zurücksetzen von Suche und Filtern bei der Rückkehr** und **der Schwierigkeit, blockierte und ungeprüfte Vorgänge herauszufiltern**. Für jedes Thema führt die Tabelle weiterhin betroffene Nutzende, Beleg-IDs, die Konfidenz, Auswirkungen auf das Design, offene Fragen und Folgemaßnahmen auf. Die Zahlen stehen für wiederholte Nennungen in einer kleinen Stichprobe, nicht für die Häufigkeit im gesamten Produkt.

</div>

## So funktioniert es

1. Nenne Work die zu prüfenden Feedbackquellen, den Produktbereich und den Zeitraum.
2. Bitte Work, wiederkehrendes Feedback nach Themen zu gruppieren und für jedes Thema die zugehörigen Links oder IDs als Belege aufzuführen.
3. Erstelle eine Google-Tabelle oder ein Google-Dokument mit Angaben zu den betroffenen Nutzenden, zur Konfidenz, zu offenen Fragen und zur erforderlichen Entscheidung oder Folgemaßnahme.
4. Prüfe die Zusammenfassung, bevor du aus einem Thema ein Slack-Update oder einen Issue-Entwurf erstellst.

Verwende für den ersten Durchlauf den Starter-Prompt auf dieser Seite. Verfeinere anschließend alle Themen, die zu breit gefasst sind, für die Belege fehlen oder die mehrere eigenständige Probleme vermischen.

## Aus einem geprüften Thema den nächsten Entwurf erstellen

Sobald die Zusammenfassung vorliegt, bitte Work, ein zu breit gefasstes Thema aufzuteilen, fehlende Belege zu ergänzen, ein Slack-Update zu entwerfen oder aus einem geprüften Thema einen Issue-Entwurf zu erstellen. Nenne die Zielgruppe und die anstehende Entscheidung, damit der nächste Schritt klar ist.

## Einen Feedbackkanal auf dem neuesten Stand halten

Wenn in einem Slack-Kanal oder einer Issue-Warteschlange laufend neue Meldungen eingehen, bitte Work, [diese Quelle nach einem Zeitplan zu prüfen](/de-DE/codex/automations#schedule-work-from-a-task). Behalte dieselben Prüfvorgaben bei, damit neues Feedback nicht ohne Genehmigung als Beitrag veröffentlicht, als Issue angelegt oder als Aufgabe zugewiesen wird.

<!-- source: https://learn.chatgpt.com/de-DE/use-cases/build-an-ai-tour-guide -->

## Einführung

Manche Arbeitsabläufe lassen sich leichter erlernen, wenn dir jemand zeigt, wohin du navigieren und was du auswählen musst. Erstelle mit Codex eine Tour, die Nutzende durch deine Web-App führt, während sie die Aktionen selbst ausführen.

Mit WebMCP-Tools für die Bedienelemente, den Zustand und die Dokumentation deiner App kann Codex die nächste Anweisung danach auswählen, was die nutzende Person gerade sieht. Wer einen Dienst noch nicht verbunden hat, braucht einen anderen ersten Schritt als jemand, der das Setup bereits abgeschlossen hat.

## So gehst du vor

1. Öffne das Repository deiner App in Codex und wähle einen Ablauf aus, durch den die Tour führen soll, etwa das Verbinden eines Dienstes oder das Hinzufügen eines Ordners.
2. Stelle die relevante Dokumentation bereit und beschreibe die Ausgangszustände, mit denen die Tour umgehen soll.
3. Führe den Einstiegs-Prompt auf dieser Seite aus, um Zielelemente für die Tour, Tools für den UI-Zustand und Zugriff auf die Anweisungen der App hinzuzufügen.
4. Teste den Ablauf in einer Browserumgebung, in der Codex die WebMCP-Tools deiner App aufrufen kann. Bitte Codex, dich anzuleiten, und führe dann jeden Schritt selbst aus.

Begrenze den Umfang der ersten Tour. Prüfe, ob sie Nutzende vom Setup bis zum Abschluss führen kann, bevor du weitere Arbeitsabläufe hinzufügst.

## Beispiel: Einen Ordner aus Google Drive in Runme hinzufügen

In <a href="https://web.runme.dev" target="_blank" rel="noopener noreferrer">Runme</a> bearbeiten Nutzende Notebooks und verwenden einen Datei-Explorer, um Ordner aus Google Drive hinzuzufügen und durch ihre Dateien zu navigieren. Die Tour hilft neuen Nutzenden, diese Bedienelemente zu finden und den Ablauf kennenzulernen.

Mehr über Runme erfährst du im Artikel <a href="https://developers.openai.com/blog/automating-repetitive-work-at-openai-with-codex" target="_blank" rel="noopener noreferrer">Wiederkehrende Aufgaben bei OpenAI mit Codex automatisieren</a>.

Sieh dir an, wie Codex die Bedienelemente von Runme hervorhebt und erklärt, wozu sie dienen. Die Screenshots unten zeigen eine separate Tour, die sich auf das Hinzufügen eines Ordners aus Google Drive konzentriert.

<figure class="not-prose my-4">
  <video
    class="w-full rounded-lg border border-default"
    controls
    muted
    playsinline
    preload="metadata"
    poster="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/tour-demo-poster.webp"
    aria-label="Codex demonstrates an AI tour of Runme's controls"
  >
    <source
      src="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/runme-ai-tour-demo.webm"
      type="video/webm"
    />
    Dein Browser unterstützt das Video-Tag nicht.
  </video>
</figure>

Die Tour für Google Drive beginnt mit einer Anfrage:

### Google Drive verbinden

Codex prüft, ob Google Drive verbunden ist. Falls nicht, hebt Codex **Google Drive verbinden** hervor und fordert die nutzende Person auf, dieses Bedienelement auszuwählen und die Verbindung herzustellen.

![Codex hebt „Google Drive verbinden“ in Runme hervor und erklärt, wie es losgeht.](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/connect-google-drive.webp)

### Datei-Explorer öffnen

Sobald die Verbindung hergestellt ist, führt Codex die nutzende Person zum Datei-Explorer. Die nächste Anweisung richtet sich nach dem aktualisierten Zustand der App.

![Codex hebt das Bedienelement hervor, mit dem sich der Datei-Explorer von Runme öffnen lässt.](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/open-file-explorer.webp)

### Ordner hinzufügen

Sobald die nutzende Person die Symbolleiste ausklappt, hebt Codex das Bedienelement zum Hinzufügen eines Ordners aus Google Drive hervor. Die Person behält die Kontrolle über die Interaktion und lernt, wo sie das Bedienelement beim nächsten Mal findet.

![Codex hebt das Bedienelement zum Hinzufügen eines Ordners aus Google Drive in Runme hervor.](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/add-google-drive-folder.webp)

## Gib Codex den nötigen Kontext, um Nutzende anzuleiten

Runme stellt in seiner Implementierung drei Arten von Kontext bereit: Zielelemente der Tour, den Anwendungszustand und die Dokumentation. Die folgenden Toolnamen stammen aus Runme. Übertrage die jeweiligen Funktionen auf deine App.

### Bedienelemente auffindbar machen

Gib den Zielelementen der Tour stabile, semantische Werte für `data-tour-id` sowie jeweils eine Bezeichnung und eine Beschreibung. Runme stellt diese Bedienelemente über drei WebMCP-Tools bereit:

- `listTargets` listet die registrierten Zielelemente, IDs, Bezeichnungen und Beschreibungen auf.
- `showTourStep({ target, title?, message, placement? })` hebt ein Zielelement hervor und zeigt eine Erklärung an.
- `dismiss` entfernt die Hervorhebung.

So kann Codex ein Bedienelement erkennen und erklären, ohne die zugehörige Aktion für die nutzende Person auszuführen.

### Zustand auslesen und auf Nutzende warten

Runme verwaltet den für die Tour relevanten Zustand außerhalb von React und stellt ihn über einen Controller bereit. Das Tool `getUiSnapshot` liefert den aktuellen UI-Zustand einschließlich des Anmeldestatus. Mit `waitForUiChange(...)` kann Codex auf eine Änderung warten, etwa darauf, dass die nutzende Person das hervorgehobene Bedienelement auswählt.

Bitte Codex, den Zustand nach jeder Interaktion erneut auszulesen. Ob die Tour zum nächsten Schritt übergeht, sollte davon abhängen, was in der App passiert ist, und nicht davon, ob Codex bereits eine Anweisung angezeigt hat.

### Anweisungen mit der App bereitstellen

Runme liefert die Markdown-Dokumentation zusammen mit der Anwendung aus und stellt sie über WebMCP bereit:

- `readInstructionsForAIAgents` erklärt, wie Codex mit der App und ihren Tools interagieren soll.
- `listDocumentation()` listet die verfügbaren Seiten und ihre Beschreibungen auf.
- `getDocumentation({ name })` gibt eine ausgewählte Seite als Markdown zurück.

Die Anweisungen und Tools für die Tour können mit der App ausgeliefert werden. Ein separates Codex-Plug-in für die Tour ist dafür nicht nötig.

## Tour überprüfen

Teste dieselbe Anfrage mit unterschiedlichen Ausgangszuständen. Prüfe, ob die Tour bereits abgeschlossene Setup-Schritte überspringt, auf die nutzende Person wartet und ihre Anleitung anpasst, wenn sich die Benutzeroberfläche ändert.

Teste auch einen abgebrochenen Schritt und ein Bedienelement, das noch nicht sichtbar ist. Codex sollte erklären, was fehlt, oder einen gültigen nächsten Schritt wählen. Codex sollte nicht behaupten, eine Aktion sei erfolgreich gewesen, nur weil es eine Schaltfläche hervorgehoben hat.

Belasse die Authentifizierung, Berechtigungsprüfungen und Aktionen der Nutzenden im bestehenden Ablauf der App. Die Tour soll Nutzenden helfen, die Benutzeroberfläche zu verstehen, ohne diese Kontrollmechanismen zu umgehen.

## Sinnvolle Folgeprompts

Sobald der erste Ablauf funktioniert, mach im selben Chat weiter:

- „Teste diese Tour, wenn Google Drive bereits verbunden ist und der Datei-Explorer geschlossen ist.“
- „Behandle den Fall, dass jemand einen Schritt abbricht und anschließend darum bittet, die Tour fortzusetzen.“
- „Füge eine Tour für \[next workflow\] hinzu und verwende dabei die vorhandenen Tour-Ziele und Tools für den App-Zustand wieder.“

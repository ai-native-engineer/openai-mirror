<!-- source: https://learn.chatgpt.com/de-DE/docs/models -->

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## Modell auswählen

Wähle in der ChatGPT-Desktop-App über das Steuerelement für Modell und Reasoning-Aufwand unter dem
Editor ein verfügbares Modell aus und passe seinen Reasoning-Aufwand an.

Ein höherer Reasoning-Aufwand kann bei komplexen Aufgaben bessere Ergebnisse liefern, benötigt aber
mehr Zeit und verbraucht mehr Token. Beginne mit der Standardeinstellung und erhöhe den Aufwand, wenn
die Aufgabe eine gründlichere Planung oder Analyse erfordert.

Der Modus <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> geht
über einen Durchlauf mit nur einem Agenten hinaus. Er nutzt
[Subagenten](/codex/agent-configuration/subagents), um komplexe Aufgaben schneller zu bearbeiten.
Damit eignet er sich für größere Aufgaben, die sich auf mehrere Subagenten verteilen lassen.

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## Modell auswählen

Diese Empfehlungen gelten für **ChatGPT Work** im Web. Wähle über das
Steuerelement für Modell und Reasoning-Aufwand unter dem Editor ein verfügbares Modell aus
und passe seinen Reasoning-Aufwand an.

Ein höherer Reasoning-Aufwand kann bei komplexen Aufgaben bessere Ergebnisse liefern, benötigt aber
mehr Zeit und verbraucht mehr Token. Beginne mit der Standardeinstellung und erhöhe den Aufwand, wenn
die Aufgabe eine gründlichere Planung oder Analyse erfordert.

Der Modus <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> geht
über einen Durchlauf mit nur einem Agenten hinaus. Er nutzt
[Subagenten](/codex/agent-configuration/subagents), um komplexe Aufgaben schneller zu bearbeiten.
Damit eignet er sich für größere Aufgaben, die sich auf mehrere Subagenten verteilen lassen.

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_minmax(22rem,25rem)] lg:items-start">
  <div class="min-w-0">

## Modell auswählen

Verwende in einer interaktiven CLI-Sitzung `/model`, um das Modell zu wechseln oder den
Reasoning-Aufwand anzupassen. Du kannst beim Start von Codex auch mit
`--model` oder dem Alias `-m` ein Modell auswählen:

Dieselbe Option funktioniert auch bei nicht interaktiven Ausführungen. Beispiel:

Ein höherer Reasoning-Aufwand kann die Ergebnisse bei komplexen Aufgaben verbessern, erfordert aber
mehr Zeit und verbraucht mehr Token. Beginne mit dem voreingestellten Reasoning-Aufwand und erhöhe ihn, wenn
die Aufgabe eine gründlichere Planung oder Analyse erfordert.

Der Modus <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> geht
über einen Durchlauf mit nur einem Agenten hinaus. Er nutzt
[Subagenten](/codex/agent-configuration/subagents), um komplexe Aufgaben schneller zu erledigen.
Damit eignet er sich für größere Aufgaben, die sich auf mehrere Subagenten verteilen lassen.

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## Modell auswählen

Verwende die Modellauswahl unter dem Editor, um ein verfügbares Modell und den
Reasoning-Aufwand auszuwählen.

Ein höherer Reasoning-Aufwand kann die Ergebnisse bei komplexen Aufgaben verbessern, erfordert aber
mehr Zeit und verbraucht mehr Token. Beginne mit dem voreingestellten Reasoning-Aufwand und erhöhe ihn, wenn
die Aufgabe eine gründlichere Planung oder Analyse erfordert.

Der Modus <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> geht
über einen Durchlauf mit nur einem Agenten hinaus. Er nutzt
[Subagenten](/codex/agent-configuration/subagents), um komplexe Aufgaben schneller zu erledigen.
Damit eignet er sich für größere Aufgaben, die sich auf mehrere Subagenten verteilen lassen.

  </div>
  
</div>

<a id="recommended-models"></a>
<a id="other-models"></a>
<a id="deprecated-codex-models"></a>
<a id="configure-your-default-local-model"></a>
<a id="choose-a-model-for-cloud-tasks"></a>
<a id="gpt-6-astra"></a>

## Empfohlene Modelle

<a id="app-compare-models"></a>

<div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
  

  

</div>

Die Verfügbarkeit hängt vom Rollout, deiner Anmeldemethode und deinem Client ab.
Informationen zu Zugriff und Nutzung in den einzelnen Tarifen findest du unter [Preise](/de-DE/codex/pricing).
Unter [Verfügbarkeit von Modellen im Workspace](/de-DE/codex/enterprise/workspace-model-availability#gpt-6-astra-in-enterprise) findest du
Informationen zum Zugriff mit Enterprise.

  Beginne mit der Standardeinstellung für Leistung, die deinem Konto zur Verfügung steht. Bewege den Regler in Richtung
**Intelligenter** für gründlicheres Nachdenken oder **Schneller** für schnelleres, kostengünstigeres Arbeiten.
  Öffne **Fortgeschritten** , wenn du `gpt-5.6-luna` oder ein bestimmtes Modell, einen bestimmten Reasoning-Aufwand
  oder eine bestimmte Geschwindigkeit auswählen möchtest.

Die Abbildungen der Modellauswahl zeigen die Bedienelemente für GPT-5.6. Für berechtigte Konten mit Pro, Business
(100 USD) und Enterprise werden die Leistungsoptionen mit dem Astra-Rollout
auf Terra Leicht, Sol Leicht, Sol Mittel, Astra Leicht, Astra Mittel und Astra Sehr hoch
aktualisiert. Die Optionen können je nach Tarif und Rollout-Phase variieren.

### Experimentelle Kontextverwaltung

Wenn du mit ChatGPT Plus oder Pro angemeldet bist, kannst du auf unterstützten Codex-Clients die experimentelle Kontextverwaltung
aktivieren. Astra hält Notizen über mehrere Kontextfenster hinweg fest
und kann frühere Nachrichten und Tool-Ergebnisse derselben Aufgabe durchsuchen.
Diese experimentelle Funktion ist standardmäßig deaktiviert und zum Start weder mit Business oder Enterprise noch bei
Anmeldung per API-Schlüssel verfügbar.

Um die Funktion zu aktivieren, trage `features.context_management.experimental_mode = true` in deine
`config.toml` ein und starte dann eine neue Aufgabe. Informationen zur Einstellung findest du in der [Konfigurationsreferenz](/de-DE/codex/config-file/config-reference)
und zum Speicherort der Datei unter [Grundlagen der Konfiguration](/de-DE/codex/config-file/config-basic).
Die Vorgaben deines Workspace gelten weiterhin.

<a id="choosing-sol-terra-and-luna"></a>

## Zwischen Astra, Sol, Terra und Luna wählen

Wähle **Astra** , wenn eine Aufgabe über mehrere Schritte
und Tools hinweg höchste Leistungsfähigkeit erfordert. **Sol** bietet Gründlichkeit und Feinschliff, **Terra** eignet sich für alltägliche Aufgaben
und **Luna** für klare, wiederholbare Aufgaben.

### Stärken der einzelnen Modelle

- **Astra für die anspruchsvollsten Aufgaben von Anfang bis Ende.** Wähle Astra für vollständige Arbeitsabläufe
  rund um Code, Apps und Recherche, die durchgehend gründliches Nachdenken und Urteilsvermögen erfordern.
  Stelle die Quellen, Vorlagen, Rahmenbedingungen und Prüfkriterien bereit, die festlegen,
  was ein brauchbares Ergebnis ausmacht. Astra kann besser gezielte Fragen stellen und deine Hinweise
  einbeziehen, ohne dabei das ursprüngliche Ziel und die Rahmenbedingungen aus dem Blick zu verlieren.
- **Sol für komplexe Aufgaben mit offenem Ergebnis.** Wähle Sol für unklar definierte, schwierige oder
  besonders wichtige Aufgaben, die zusätzliche Analysen, Urteilsvermögen oder Feinschliff erfordern, etwa
  komplexe Codeänderungen, Deep Research oder sorgfältig ausgearbeitete Dokumente. Lege bei enger umrissenen
  Aufgaben klare Abschlusskriterien fest, damit die Arbeit fokussiert bleibt.
- **Terra, der pragmatische Allrounder.** Wähle Terra für alltägliche Aufgaben,
  die gründliches Nachdenken und einen sicheren Umgang mit Tools erfordern, wenn du nicht die volle Tiefe von Sol brauchst.
  Für Aufgaben, die du bisher GPT-5.5 übertragen hast, ist Terra ein naheliegender Ausgangspunkt.
- **Luna für klare, wiederholbare Aufgaben.** Wähle Luna für konkrete Aufgaben in großer Zahl,
  wenn du weißt, wie ein gutes Ergebnis aussieht. Beispiele sind Extraktion,
  Klassifizierung, Transformation und strukturierte Zusammenfassungen.

### Reasoning-Aufwand wählen

Wähle den niedrigsten Reasoning-Aufwand, der das gewünschte Ergebnis liefert. Erhöhe ihn
bei Aufgaben, die mehr Planung, Analyse oder Überprüfung erfordern.

- Die Einstellung **Leicht** in der ChatGPT-Desktop-App, in ChatGPT Work im Web und in der IDE-Erweiterung beziehungsweise **Niedrig** in der
  CLI eignet sich für schnelle, klar umrissene Aufgaben.
- **Mittel** bietet bei Aufgaben, die mehr Planung erfordern, ein ausgewogenes Verhältnis von Geschwindigkeit und Tiefe.
- **Hoch** und **Sehr hoch** eignen sich für schwierige Aufgaben mit mehreren Schritten, Quellen
  oder Zielkonflikten.

Die Einstellungen für den Reasoning-Aufwand von GPT-5.5 lassen sich nicht exakt auf GPT-5.6 übertragen. Probiere eine
vertraute Aufgabe mit einer niedrigeren Einstellung aus und passe diese anhand des Ergebnisses an.

### Wann Max oder Ultra sinnvoll ist

**Max** gibt dem ausgewählten Modell mehr Zeit, eine einzelne Aufgabe gründlich zu durchdenken. Verwende Max
für die schwierigsten Probleme, wenn Gründlichkeit wichtiger ist als Geschwindigkeit oder geringer Verbrauch.
Wenn Max nicht zur Auswahl steht, musst du es in den App-Einstellungen aktivieren.

**Ultra** verwendet [Subagenten](/de-DE/codex/agent-configuration/subagents), um
verschiedene Teile einer komplexen Aufgabe parallel zu bearbeiten. Wähle Ultra, wenn sich die
Arbeit in sinnvolle Teile aufteilen lässt. Für die meisten Aufgaben brauchst du weder Max noch Ultra.

Wenn Ultra im Schieberegler für die Modellauswahl der Desktop-App nicht angezeigt wird, öffne
**Einstellungen** \> **Konfiguration** und aktiviere dann **Ultra im Schieberegler für die Modellauswahl**.

## Weitere Modelle

Wenn du dich mit ChatGPT anmeldest, funktioniert Codex am besten mit den oben empfohlenen Modellen.

  <strong>
    GPT-5.4 und GPT-5.4 mini werden am 31. August 2026 aus Codex entfernt.
  </strong>{" "}
  Wenn du dich mit ChatGPT anmeldest, ersetze `gpt-5.4` durch `gpt-5.6-terra` und
`gpt-5.4-mini` durch `gpt-5.6-luna` in gespeicherten Konfigurationen, benutzerdefinierten Agenten und
  geplanten Aufgaben. Die OpenAI API und Codex mit Authentifizierung über deinen eigenen API-Schlüssel sind
  nicht betroffen.

  <div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
    

    

    

  </div>

Du kannst Codex passend zu deinem Anwendungsfall auch mit beliebigen Modellen und Anbietern verwenden, die entweder die [Chat Completions API](https://platform.openai.com/docs/api-reference/chat) oder die [Responses API](https://platform.openai.com/docs/api-reference/responses) unterstützen.

  Die Unterstützung für die Chat Completions API gilt als veraltet und wird in
künftigen Versionen von Codex entfernt.

## Veraltete Codex-Modelle

Die Modelle `gpt-5.4` und `gpt-5.4-mini` sind bei der Anmeldung mit ChatGPT
ab dem 31. August 2026 nicht mehr in Codex verfügbar. Ersetze `gpt-5.4` durch `gpt-5.6-terra` und
`gpt-5.4-mini` durch `gpt-5.6-luna` in den Standardeinstellungen deines Workspaces, gespeicherten Modelleinstellungen,
verwalteten Konfigurationen, benutzerdefinierten Agenten und geplanten Aufgaben.

Die Modelle `gpt-5.2` und `gpt-5.3-codex` gelten in Codex bereits als veraltet, wenn
du dich mit ChatGPT anmeldest. Aktualisiere Skripte, Konfigurationsdateien und
Befehle mit `codex exec --model`, die noch auf diese Modelle verweisen.

Die OpenAI API und die Nutzung von Codex mit deinem eigenen API-Schlüssel sind
von der Einstellung von GPT-5.4 nicht betroffen. Welche Modelle aktuell über die API verfügbar sind, erfährst du auf der
[Seite zu API-Modellen](/api/docs/models).

## Dein Standardmodell für die lokale Nutzung konfigurieren

Die ChatGPT-Desktop-App, Codex CLI und die IDE-Erweiterung verwenden dieselbe
[Konfigurationsdatei](/de-DE/codex/config-file/config-basic) `config.toml`. Um ein Modell festzulegen, füge deiner Konfigurationsdatei
einen Eintrag für `model` hinzu. Wenn du kein Modell festlegst, verwendet die
ChatGPT-Desktop-App, Codex CLI oder die IDE-Erweiterung ein empfohlenes Modell.

## Ein Modell für Cloud-Chats auswählen

Derzeit kannst du das Standardmodell für Chats in Codex Cloud nicht ändern.

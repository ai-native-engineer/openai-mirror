<!-- source: https://learn.chatgpt.com/de-DE/docs/browser -->

Browser ist weder in der Codex CLI noch in der Codex IDE-Erweiterung verfügbar. Öffne die ChatGPT-Desktop-App, um den integrierten Browser zu verwenden.

Mit Browser kann ChatGPT Websites öffnen, aktuelle Informationen zusammentragen und Aktionen ausführen, während du die Kontrolle behältst. Nutze ihn, um Optionen zu vergleichen, eine mehrstufige Aufgabe auf einer Website zu erledigen oder eine Seite zu überprüfen, die du gerade entwickelst.

Browser ist in ChatGPT im Web und in der ChatGPT-Desktop-App verfügbar.

[GPT-6 Astra](/de-DE/codex/models#gpt-6-astra) beurteilt visuelle Inhalte besser, etwa wenn
es eine Seite mit einem Screenshot abgleicht oder einen Ablauf über mehrere Websites hinweg ausführt.
Wähle es aus, wenn es in deiner Modellauswahl verfügbar ist, und beschreibe,
wie das fertige Ergebnis überprüft werden soll.

In verwalteten Desktop-Umgebungen können Administrierende die Origins im Browser,
Uploads, Downloads und den Zugriff auf Entwicklungsfunktionen einschränken. Siehe
[Browsersteuerung in verwalteten Umgebungen](/de-DE/codex/enterprise/managed-configuration#control-browser-and-computer-use).

Betrachte Seiteninhalte als nicht vertrauenswürdigen Kontext. Prüfe die Website und die vorgeschlagene Aktion, bevor du vertrauliche Informationen weitergibst oder ChatGPT eine Aktion ausführen lässt.

Der integrierte Browser in der ChatGPT-Desktop-App bietet dir und ChatGPT in einem Chat eine gemeinsame Ansicht von Websites und lokalen Web-Apps. Nutze ihn, um eine Seite in der Vorschau anzuzeigen, visuelles Feedback zu hinterlassen oder ChatGPT in deinem Namen mit einer Website interagieren zu lassen.

Der integrierte Browser verwendet ein Browserprofil, das von deinem üblichen
Browser getrennt ist. Er übernimmt deine bestehenden Tabs oder deine Browsersitzung nicht automatisch.
Wenn eine Aufgabe ein Konto erfordert, kannst du dich direkt anmelden. Öffne **Einstellungen \>
Browser** , um Browserdaten und alle auf deinem Gerät verfügbaren
Funktionen zum Profilimport zu verwalten.

Browser-Downloads werden standardmäßig im Downloads-Ordner deines Systems gespeichert. Unter **Einstellungen \>
Browser** kannst du einen anderen Speicherort für Downloads auswählen, ihn auf den Systemstandard zurücksetzen
oder **Nach dem Speicherort für Downloads fragen** aktivieren.

Verwende stattdessen die [Browsererweiterung](/de-DE/codex/chrome-extension), wenn ChatGPT
in einem vorhandenen Tab in Chrome, Edge, Brave, Opera oder Vivaldi arbeiten oder
dein übliches Browserprofil verwenden soll.

Öffne den integrierten Browser über die Symbolleiste, klicke auf eine URL, navigiere
manuell oder drücke <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd>
(<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd> unter Windows).

  
    
  

## Über die Adressleiste suchen

Gib Text in die Adressleiste des integrierten Browsers ein, um Seiten aus seinem Browserverlauf zu finden. Wähle eine passende Seite aus, um sie erneut zu öffnen. Gibt es keinen passenden Verlaufseintrag, gib einen Suchbegriff ein, um mit Google zu suchen.

Der integrierte Browser verwendet ein eigenes Profil und speichert einen eigenen Browserverlauf. Die Ergebnisse enthalten nicht automatisch Seiten aus deinem üblichen Chrome-Profil oder anderen Browsern.

## Browserverlauf verwalten

Öffne **Einstellungen \> Browser** , um den Verlauf des integrierten Browsers zu durchsuchen, eine
besuchte Seite erneut zu öffnen oder Verlaufseinträge zu entfernen, sofern deine Organisation dies zulässt. Mit
**Browserdaten löschen** kannst du einen Zeitraum und die Arten von Browserdaten auswählen,
die du entfernen möchtest.

Wenn diese Funktion verfügbar ist, kann ChatGPT dich bitten, deinen Browserverlauf durchsuchen zu dürfen, um eine für die aktuelle Aufgabe relevante Seite zu finden. Prüfe die Anfrage, bevor du den Zugriff erlaubst. Der Browserverlauf kann interne URLs, Suchbegriffe und andere vertrauliche Informationen enthalten. Erlaube den Zugriff daher nur, wenn die Aufgabe diesen Kontext erfordert.

<a id="browser-use"></a>

## Computernutzung im Browser

In der Desktop-App können ChatGPT Work oder Codex mit der Computernutzung den integrierten Browser direkt bedienen. Je nach deiner Auswahl kann ChatGPT Work oder Codex Seiten öffnen, klicken, Text eingeben, den gerenderten Zustand prüfen, Screenshots erstellen und das Ergebnis seiner Arbeit auf der Seite überprüfen.

Browser ist in der Desktop-App enthalten und wird automatisch installiert. Bitte ChatGPT
oder Codex, den integrierten Browser für deine Aufgabe zu verwenden, oder verweise mit
`@Browser` direkt darauf.

Zum Beispiel:

```text
Use the browser to open http://localhost:3000/settings, reproduce the layout
bug, and fix only the overflowing controls.

ChatGPT fragt nach, bevor es eine Website verwendet, es sei denn, du hast diese
Website bereits zugelassen. Verwalte zugelassene und blockierte Websites unter **Einstellungen \> Browser**. ChatGPT
fragt außerdem vor sensiblen Aktionen nach deiner Bestätigung, etwa beim Übermitteln von Informationen,
bei einem Kauf, beim Ändern von Berechtigungen oder beim Löschen von Daten. ChatGPT kann
Datei-Uploads im integrierten Browser nicht automatisieren.

  Anweisungen auf einer Seite können irreführend oder böswillig sein. Eine Berechtigung für eine Website erlaubt ChatGPT, mit ihr zu interagieren. Sie macht die Inhalte der Website nicht vertrauenswürdig und genehmigt nicht automatisch jede Aktion.

## Eine Seite in der Vorschau anzeigen

1. Starte den Entwicklungsserver deiner App im [integrierten Terminal](/de-DE/codex/integrated-terminal) oder über eine [Aktion in der lokalen Umgebung](/de-DE/codex/environments/local-environment#actions).
2. Öffne die lokale Route, die dateibasierte Seite oder die öffentliche Seite, indem du auf eine URL klickst oder im Browser manuell dorthin navigierst.
3. Prüfe den gerenderten Zustand zusammen mit dem Code-Diff.
4. Hinterlasse Browserkommentare zu den Elementen oder Bereichen, die geändert werden müssen.
5. Bitte ChatGPT, die Kommentare umzusetzen und den Umfang der Änderungen eng zu begrenzen.

Zum Beispiel:

```text
I left comments on the pricing page in the built-in browser. Address the mobile
layout issues and keep the card structure unchanged.

## Die Seite kommentieren

Wenn ein Fehler nur auf der gerenderten Seite sichtbar ist, gib ChatGPT mit Browserkommentaren präzises Feedback.

1. Aktiviere den **Anmerkungsmodus**.
2. Klicke auf ein Element oder wähle durch Ziehen einen Bereich aus.
3. Verfasse und speichere deinen Kommentar.
4. Sende im Chat eine Nachricht und bitte ChatGPT, die Kommentare umzusetzen.

Am hilfreichsten sind Kommentare, wenn du das Problem und das gewünschte Ergebnis benennst:

```text
This button overflows on mobile. Keep the label on one line if it fits,
otherwise wrap it without changing the card height.

```text
This tooltip covers the data point under the cursor. Reposition the tooltip so
it stays inside the chart bounds.

<section class="feature-grid">

<div>

### Feedback zur Gestaltung

Wenn du einem Abschnitt der Seite eine Anmerkung hinzufügst, wähle **Anpassen** neben
dem Texteingabefeld aus, um ChatGPT detaillierteres Feedback zur Gestaltung zu geben. Du kannst
Werte wie Schriftart, Text, Abstände und Farbe ändern, das Ergebnis auf der Seite in der Vorschau ansehen
und die Anmerkung anschließend mit einer präziseren Zielvorgabe senden.

</div>

  
    
  

</section>

## Browseraufgaben klar eingrenzen

Begrenze jede Browseraufgabe so, dass du sie in einem Durchgang prüfen kannst.

- Nenne die Seite, Route oder URL.
- Gib an, welcher Zustand dir wichtig ist, etwa „Laden“, „Leer“, „Fehler“ oder „Erfolg“.
- Hinterlasse Kommentare genau an den Elementen oder Bereichen, die geändert werden müssen.
- Prüfe die Seite erneut, nachdem ChatGPT fertig ist.
- Bitte ChatGPT, den Entwicklungsserver zu starten oder zu prüfen, bevor es eine lokale Seite öffnet.

Nutze bei Änderungen am Repository den [Review-Bereich](/de-DE/codex/code-review?surface=app), um
die Änderungen zu prüfen und Kommentare zu hinterlassen.

<section class="feature-grid">

<div>

## Entwicklermodus

Der Entwicklermodus funktioniert mit der Computernutzung in Chrome und im integrierten Browser. Er gewährt ChatGPT kontrollierten Zugriff auf das Chrome DevTools Protocol (CDP). Nutze ihn, um JavaScript-Profile zu erstellen, Konsolenausgaben und Netzwerkverkehr zu prüfen, das DOM und die angewendeten Stile zu untersuchen oder ein Problem im laufenden Browser zu diagnostizieren.

Um ihn zu aktivieren, öffne [**Einstellungen \> Browser**](codex://settings/browser-use) und schalte
unter **Entwicklermodus** die Option **Vollständigen CDP-Zugriff aktivieren** ein. Wenn deine
Organisation diese Einstellung deaktiviert hat, kannst du sie nicht lokal aktivieren. Administrierende können
`browser_use_full_cdp_access = false` unter `[features]` in
[`requirements.toml`](/de-DE/codex/enterprise/managed-configuration#pin-feature-flags) festlegen,
um den vollständigen CDP-Zugriff zu deaktivieren und zu verhindern, dass Nutzende die entsprechende
Einstellung in der ChatGPT-Desktop-App aktivieren.

Vollständiger CDP-Zugriff kann vertrauliche interne Browserinformationen offenlegen. ChatGPT fordert eine ausdrückliche Genehmigung an, bevor es vollständigen CDP-Zugriff zur Untersuchung einer Website verwendet. Prüfe die Website, die Aufgabe und den angeforderten Zugriff, bevor du ihn genehmigst.

Verwende `@Browser` für den integrierten Browser. Um den Entwicklermodus in Chrome zu verwenden,
[richte die Chrome-Erweiterung ein](/de-DE/codex/chrome-extension) und rufe `@Chrome` auf.

Zum Beispiel:

```text
This app is slow. Use @Browser to capture a performance trace and inspect
network traffic, then identify the bottleneck.

</div>

  
    
  

</section>

## Mit ChatGPT Work Aufgaben im Web erledigen

ChatGPT Work kann Aufgaben über mehrere Websites hinweg erledigen, auch auf Websites, bei denen du dich anmelden musst.

Work verwendet einen eigenen Browser auf einem separaten Computer in der Cloud, nicht den Browser auf deinem Smartphone oder Laptop.

Starte eine Aufgabe in ChatGPT Work im Web oder auf einem Mobilgerät. ChatGPT kann weiterarbeiten, auch wenn du weggehst und deinen Computer zuklappst. Mit seinem Computer kann Work verschiedenste Aufgaben im Internet erledigen, indem es Webseiten liest, Elemente anklickt und Text eingibt. Je nach deiner Anfrage nutzt es dafür ein Plug-in, seinen Browser oder beides.

ChatGPT kann dir zum Beispiel bei folgenden Aufgaben helfen:

- Einen Termin beim DMV finden und buchen.
- Dich in deinem Kundenkonto beim Versorgungsunternehmen anmelden und Tarife vergleichen.
- Wohnungsangebote finden und speichern, die deinen Kriterien entsprechen.
- Informationen über die Konkurrenz in sozialen Medien recherchieren.
- Die Bücher in deiner Buchhaltungssoftware abschließen.

Du entscheidest, auf welche Websites ChatGPT zugreifen darf. Es ist darauf trainiert, vor folgenreichen Aktionen wie dem Abschluss einer Buchung oder einer Zahlung um Bestätigung zu bitten. Falls ChatGPT aus irgendeinem Grund nicht weiterkommt, kannst du seinen Computer auf Mobilgeräten und auf dem Desktop übernehmen und selbst bedienen.

Mit den Plänen Plus und Pro kann ChatGPT Work im Web und auf Mobilgeräten Websites aufrufen, die eine Authentifizierung erfordern.

Die Verfügbarkeit hängt von der schrittweisen Einführung ab. Für Workspaces mit ChatGPT Enterprise oder ChatGPT Edu ist die Anmeldung auf Websites nicht verfügbar.

## So funktioniert der Computer von ChatGPT Work

Wenn deine Aufgabe eine Website erfordert, nutzt ChatGPT seinen eigenen Browser, um dort zu navigieren, Informationen zu sammeln und Schritte online auszuführen.

Standardmäßig fragt ChatGPT nach, bevor es auf eine neue Website zugreift. Du kannst Anfragen einzeln genehmigen oder deine Einstellungen so anpassen, dass ChatGPT den Zugriff auf Websites, die für deine Aufgabe relevant sind, automatisch genehmigen kann. ChatGPT Work fragt vor folgenreichen Aktionen immer nach deiner Bestätigung, etwa bevor es deine Daten für eine Terminbuchung übermittelt oder eine Zahlung abschließt.

## Auf einer Website anmelden

Wenn du dich auf einer Website anmelden musst, fordert ChatGPT Work dich dazu auf. Nach der Authentifizierung arbeitet es auf der Website weiter, auf der du nun angemeldet bist. Deine Sitzung bleibt für künftige Aufgaben aktiv, sodass du dich nicht jedes Mal neu anmelden musst.

### Das sichere Anmeldeformular verwenden

ChatGPT kann weder deinen Nutzernamen noch dein Passwort sehen. Diese Daten sind für das Modell nie sichtbar und werden nicht für das Modelltraining verwendet. ChatGPT speichert weder deinen Nutzernamen noch deine Passwörter. Du kannst deinen Browserverlauf jederzeit unter **Einstellungen** \> **Cloud-Browser** \> **Browserdaten** für alle Websites oder für einzelne Websites löschen. Dabei wirst du von der jeweiligen Website abgemeldet.

Wenn ChatGPT auf eine Anmeldeseite stößt, hält es die Aufgabe an und fordert dich auf, deine Zugangsdaten und bei Bedarf Codes für die Zwei-Faktor-Authentifizierung einzugeben. Unter iOS kannst du dich bequem mit einem unterstützten Passwortmanager anmelden.

Verwende das von ChatGPT bereitgestellte Anmeldeformular. Sende keine Passwörter im Chat.

![ChatGPT Work unter iOS pausiert eine DMV-Aufgabe und zeigt ein sicheres Anmeldeformular mit der Website-Adresse und einem verdeckt dargestellten Passwort an.](/images/codex/cloud-browser-auth/sign-in.webp)

### Auf der Webseite anmelden

Wenn die Option **Stattdessen auf der Webseite anmelden** verfügbar ist, wähle sie aus, um dich direkt im Cloud-Browser anzumelden. Die Aufgabe pausiert, während du dich anmeldest. Wähle **Ich bin fertig** , um die Steuerung wieder an ChatGPT zu übergeben. Alternativ kannst du die Anfrage überspringen oder abbrechen.

<a id="start-a-browser-task"></a>
<a id="start-browser-work"></a>
<a id="web-start-browser-work"></a>

## So startest du eine Aufgabe in ChatGPT Work

1. Öffne ChatGPT im Web oder auf einem Mobilgerät und starte eine Aufgabe in Work.
2. Beschreibe, was ChatGPT tun soll.
3. Genehmige den Zugriff auf die Website, wenn du dazu aufgefordert wirst.
4. Melde dich direkt an, wenn eine Website dies erfordert.
5. Verfolge den Fortschritt der Aufgabe in der Unterhaltung.
6. Prüfe das Ergebnis und genehmige alle folgenreichen Aktionen.

Du musst den Browser nicht separat auswählen. ChatGPT entscheidet anhand deiner Anfrage, wann es ihn verwendet.

Einige Websites blockieren den Zugriff. In diesem Fall informiert dich ChatGPT und versucht, wenn möglich, die Aufgabe auf einem anderen Weg zu erledigen.

<a id="website-permissions-and-confirmations"></a>
<a id="web-website-permissions-and-confirmations"></a>

## Sicherheit und deine Kontrollmöglichkeiten

Öffne in den ChatGPT-Einstellungen **Cloud-Browser** , um die Berechtigungen für Websites zu verwalten. Zu den verfügbaren Optionen gehören:

- **Immer fragen**: Prüfe jede Anfrage für den Zugriff auf eine Website manuell.
- **Automatisch genehmigen**: Lass ChatGPT den Zugriff automatisch genehmigen, nachdem es geprüft hat, ob die Website für deine Aufgabe relevant ist.
- **Immer erlauben**: Erlaube den Zugriff auf Websites ohne diesen zusätzlichen Prüfschritt. Wir bieten diese Option für einen möglichst reibungslosen Ablauf an, empfehlen sie aber nicht.

![Einstellungen des Cloud-Browsers mit den Optionen „Immer fragen“, „Automatisch genehmigen“ und „Immer erlauben“ für den Zugriff auf Websites.](/images/codex/cloud-browser-auth/website-permissions.webp)

Du kannst auch einzelne Websites erlauben oder blockieren und so deine Standardberechtigungen für diese Websites überschreiben.

Bevor ChatGPT dich auffordert, dich auf einer Website anzumelden, prüft ein zusätzliches Modell, ob die Anmeldeanfrage oder die Seite, auf der deine Daten eingegeben werden sollen, Anzeichen für Phishing oder Täuschung aufweisen. Wir testen den Agenten unter anderem auf Risiken durch Prompt Injection, Phishing und unbeabsichtigte Aktionen.

Für volle Transparenz siehst du die Adresse der Website und eine Vorschau ihres Anmeldeformulars. Außerdem kannst du die Website direkt prüfen, bevor du fortfährst. Zugangsdaten, die du über das sichere Anmeldeformular eingibst, werden direkt an den Browser übermittelt und sind für das Modell nicht sichtbar.

<a id="browser-data"></a>
<a id="web-browser-data"></a>

## Datenschutz und Browserdaten

Der Computer von ChatGPT Work läuft getrennt vom Browser auf deinem Gerät. Er verwaltet eigene Cookies, Browserdaten und angemeldete Sitzungen. Für die Informationen, die ChatGPT beim Bearbeiten einer Aufgabe verwendet, gelten die von dir gewählten Einstellungen zur Datenkontrolle in ChatGPT. Du kannst sie in ChatGPT im Web und auf Mobilgeräten unter **Einstellungen** \> **Datenkontrollen** einsehen.

Er nutzt weder offene Tabs noch den Browserverlauf, gespeicherte Passwörter, Cookies, Erweiterungen oder bestehende angemeldete Sitzungen deines persönlichen Browsers.

Um Browserdaten zu löschen, gehe zu **Einstellungen** \> **Cloud-Browser** \> **Browserdaten** \> **Alle löschen**. Dadurch wirst du im Browser von ChatGPT Work von den Websites abgemeldet und musst dich für künftige Aufgaben erneut anmelden.

![Einstellungen des Cloud-Browsers mit dem Abschnitt „Browserdaten“ und der Einstellung „Cookies“ zur Verwaltung der im Cloud-Browser gespeicherten Cookies.](/images/codex/cloud-browser-auth/browser-data.webp)

## Einschränkungen

- Die Anmeldung auf Websites ist nicht in jedem Workspace oder in jeder Phase der Einführung verfügbar. Wenn eine Aufgabe eine nicht unterstützte Anmeldemethode erfordert, erledige diesen Schritt selbst oder verwende ein anderes verfügbares Tool.
- Einige Websites blockieren automatisierte Browser oder verlangen ein CAPTCHA. ChatGPT kann Aufgaben auf diesen Websites möglicherweise nicht abschließen.
- Die Verfügbarkeit des Cloud-Browsers kann von deinem Plan, deinen Workspace-Einstellungen und der schrittweisen Einführung abhängen. Der Cloud-Browser ist in allen Regionen mit kostenpflichtigen Plänen außer Free und Go verfügbar. Bei ChatGPT Enterprise müssen Administrierende den Cloud-Browser für ihren Workspace aktivieren.

Während der Einführung wird der Browser möglicherweise nicht sofort angezeigt, auch wenn dein Plan ihn unterstützt.

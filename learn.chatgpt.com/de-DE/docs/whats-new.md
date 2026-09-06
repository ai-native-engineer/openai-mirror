<!-- source: https://learn.chatgpt.com/de-DE/docs/whats-new -->

Dieser wöchentliche Überblick stellt Funktionen von ChatGPT und Codex vor, die deine
Arbeitsweise verändern können, und bietet Beispiele sowie weiterführende Links. Alle Updates mit Versionsnummer, Fehlerbehebungen
und kleineren Verbesserungen findest du im [Codex-Änderungsprotokoll](/codex/changelog).

## 31. August bis 4. September 2026

### Anspruchsvolle Aufgaben mit GPT-6 Astra angehen

[GPT-6 Astra](/de-DE/codex/models#gpt-6-astra) verbindet fortgeschrittenes logisches Denken, Computernutzung
und besseres Urteilsvermögen für komplexe Programmieraufgaben, die Arbeit mit Apps und Recherchen in
Codex und ChatGPT Work. Nutze es, um einen Ablauf auszuführen, das Ergebnis zu prüfen und
ein Dokument, eine Tabelle oder eine Präsentation zu erstellen, die zu deinen Vorlagen und
deiner Aufgabe passt.

Sobald Astra für dein Konto verfügbar ist, wähle es in der Modellauswahl aus.
Informiere dich über [Nutzung und Preise](/de-DE/codex/pricing), bevor du eine umfangreiche Aufgabe startest.
Der Zugang mit Enterprise setzt voraus, dass dein Konto für den Rollout berechtigt ist
und die Administration Astra aktiviert.

## 24.–28. August 2026

### Mit mehr Websites arbeiten

- **Nutze deinen Browser:** Arbeite von der ChatGPT-Desktop-App aus mit [Edge, Brave, Opera oder Vivaldi](/de-DE/codex/chrome-extension)
  sowie mit Chrome. Füge einen geöffneten Tab zu einem Chat in ChatGPT Work oder Codex hinzu
  und arbeite mit der Website, bei der du bereits angemeldet bist.
  Opera unterstützt die Browsersteuerung, bietet aber keinen Chat in der Seitenleiste.

- **Nutze die Tools einer Website:** Mit [Website-Tools (WebMCP)](/de-DE/codex/webmcp) können ChatGPT Work
  und Codex im integrierten Browser der Desktop-App Aktionen nutzen,
  die eine Website anbietet. Ein Dokumenteditor kann zum Beispiel Tools bereitstellen,
  um einen Abschnitt zu finden oder einen Kommentar hinzuzufügen. Aktualisiere die Desktop-App und nutze
  GPT-5.6 Sol oder GPT-5.6 Terra. Website-Tools sind weder mit GPT-5.6 Luna noch in
  Enterprise- oder Edu-Workspaces verfügbar.

- **Melde dich über den Cloud-Browser an:** Mit einem berechtigten Tarif kannst du in ChatGPT Work
  im Web, unter iOS oder Android eine Aufgabe fortsetzen, für die ein Website-Konto erforderlich ist.
  Folge der [Aufforderung zur Anmeldung](/de-DE/codex/browser?surface=web#web-sign-in-to-a-website)
  und gib deine Daten im Anmeldeprozess ein, nicht im Chat. Dein lokales Browserprofil
  wird dadurch nicht verbunden. Die Anmeldung bei Websites ist in
  Enterprise- oder Edu-Workspaces nicht verfügbar.

Die Verfügbarkeit hängt vom Rollout und den Workspace-Einstellungen ab.

[Lies die Versionshinweise zum Browser
vom 25. August](/codex/changelog#codex-2026-08-25-browser).

### Geplante Aufgaben durch App-Ereignisse starten

[Geplante Aufgaben](/de-DE/codex/automations?surface=web#web-trigger-tasks-from-app-events) können jetzt starten,
wenn in Gmail, Slack oder GitHub ein unterstütztes Ereignis eintritt. Nutze einen Ereignisauslöser,
um neue E-Mails zu sichten und zu priorisieren, Kanalaktivitäten zusammenzufassen oder auf Feedback zu Pull Requests
zu reagieren, ohne dafür in festen Abständen Abfragen durchzuführen.

Mit einem berechtigten Tarif sind ereignisgesteuerte Aufgaben in ChatGPT im Web und auf Mobilgeräten verfügbar.
Verbinde zuerst die entsprechende App und genehmige den von ihr angeforderten Zugriff. In verwalteten
Workspaces kann die Administration den Zugriff steuern.

<PromptComponent
  prompt={`Wenn einer meiner Pull Requests in <owner>/<repository> neues Review-Feedback erhält, fasse das Feedback zusammen und erstelle einen Überarbeitungsplan.`}
/>

[Lies die Versionshinweise
vom 25. August](/codex/changelog#codex-2026-08-25-event-triggers).

## 17.–21. August 2026

### Mit mehr deiner Apps und Inhalte arbeiten

- **Apple Messages:** [Finde Chats, fasse Nachrichten zusammen, bereite Antworten vor und sende sie über Messages auf deinem Mac](/de-DE/codex/plugins?surface=app#app-use-apple-messages-from-codex). Das Plug-in ist mit allen Tarifen in der ChatGPT-Desktop-App für macOS verfügbar. Nutze es in ChatGPT Work und Codex, nicht in regulären ChatGPT-Chats. Standardmäßig sendet ChatGPT Nachrichten erst, nachdem du die Nachricht und den Empfängerkreis genehmigt hast.

- **Sites gemeinsam bearbeiten:** Sofern verfügbar, kannst du [aktive Mitglieder deines Workspaces zur Bearbeitung einladen](/de-DE/codex/sites#collaborate-on-a-site). Sobald die Person, der die Site gehört, sie erstmals veröffentlicht hat, können eingeladene Bearbeitende die Site weiterentwickeln und Updates veröffentlichen. Sie können die Daten aus der Live-Datenbank der Site einsehen; wer die Site besitzt, behält die Kontrolle über Freigaben und Einstellungen.

- **Änderbare Site-URLs:** Sofern verfügbar, kannst du [für eine bestehende Site eine neue von ChatGPT gehostete Adresse wählen](/de-DE/codex/sites#change-a-site-url), ohne die Site erneut bereitzustellen. Die bisherige Adresse leitet auf die neue weiter.

- **Verlauf der Computernutzung in Europa:** Nutze den [Verlauf der Computernutzung](/de-DE/codex/customization/computer-history) im EWR, in der Schweiz und im Vereinigten Königreich. Für alle, die ChatGPT Pro, Business oder Enterprise unter macOS nutzen, bleibt die Funktion standardmäßig deaktiviert. Bei Business und Enterprise muss die Administration den Zugriff zuerst aktivieren.

- **Geteilte Thread-Snapshots:** [Teile einen Snapshot eines lokalen Codex-Threads ohne Schreibzugriff](/de-DE/codex/use-chatgpt#share-a-read-only-snapshot-of-a-codex-thread) über die ChatGPT-Desktop-App für macOS. Links aus persönlichen Konten sind für alle aufrufbar, die den Link besitzen; Links aus Workspace-Konten sind auf den Workspace beschränkt, aus dem sie stammen. Codex schwärzt Geheimnisse anhand bekannter Muster. Prüfe den Snapshot trotzdem vor dem Teilen, da sensible Inhalte verbleiben können.

- **Synchronisierte angepinnte Threads:** Halte deine [angepinnten Chats](/de-DE/codex/projects?surface=app#app-organize-projects-and-chats) auf dem Desktop und unter iOS synchron.

[Lies die Versionshinweise vom 20. August](/codex/changelog#codex-2026-08-20-app).

### Mit GitLab-Projekten in Codex Cloud arbeiten

Die [GitLab-Unterstützung](/de-DE/codex/third-party/gitlab) ist in allen ChatGPT-Tarifen als Betaversion
verfügbar. Verbinde ein Projekt, erstelle eine Cloud-Umgebung und starte Aufgaben aus Issues
oder Merge Requests mit `@codex`. Fordere einmalige oder automatische Reviews
für Merge Requests an.

Die Integration läuft in Codex Cloud und kann in verwalteten Workspaces von der
Administration deaktiviert werden. Durch GitLab ausgelöste Aktivitäten setzen die Berechtigung voraus,
den jeweiligen Webhook zu konfigurieren. Verbindungen mit GitLab Self-Managed und GitLab Dedicated müssen von der
Workspace-Administration eingerichtet werden; Webhook-Aktivitäten erfordern GitLab 19.0 oder neuer.

[Lies die GitLab-Versionshinweise
vom 19. August](/codex/changelog#codex-2026-08-19-gitlab).

### Metadaten öffentlicher Plug-ins zur Überprüfung exportieren

Berechtigte Workspace-Inhabende und Admins von ChatGPT Enterprise können eine CSV-Datei mit
den öffentlichen Plug-ins herunterladen, die in ihrem Workspace sichtbar sind. Wähle unter
[Admin \> Plug-ins](https://chatgpt.com/admin/plugins) zuerst **Öffentlich** und dann
das Download-Symbol (**CSV exportieren**) aus.

Der Export enthält Namen und Beschreibungen von Plug-ins, Apps und Chat-Skills sowie
Angaben zu den Entwickelnden, zur Version und zum Datum der Aufnahme in UTC sowie Metadaten zur Verifizierung durch OpenAI.
Er basiert auf einem Snapshot des öffentlichen Katalogs, der bis zu 48 Stunden alt sein kann, und enthält keine
Plug-ins, die für den Workspace erstellt wurden. Der Export ist in FedRAMP-Workspaces
nicht verfügbar.

[Lies die Versionshinweise zum Admin-Export
vom 17. August](/codex/changelog#codex-2026-08-17-admin-csv).

## 10.–14. August 2026

### Frühere Arbeiten mit dem Verlauf der Computernutzung finden

Der [Verlauf der Computernutzung](/de-DE/codex/customization/computer-history) erstellt aus deinen Aktivitäten
in Apps und auf Websites eine durchsuchbare Zeitleiste und Erinnerungen, die ChatGPT
und Codex nutzen können. Aktiviere die Funktion nur, wenn du diesen Kontext teilen möchtest. Danach kannst du
auswählen, welche Apps und Websites berücksichtigt werden, die Erfassung pausieren und deinen Verlauf jederzeit
prüfen oder löschen.

Der Verlauf der Computernutzung ist in der ChatGPT-Desktop-App unter macOS für
ChatGPT Pro, Business und Enterprise verfügbar. Bei Business und Enterprise muss die
Administration den Zugriff zuerst aktivieren. Zunächst ist die Funktion nicht in der
Europäischen Union, der Schweiz und dem Vereinigten Königreich verfügbar.

### ChatGPT-Desktop-App unter Linux nutzen

Die [ChatGPT-Desktop-App für Linux](/de-DE/codex/linux/linux-app) ist jetzt als Vorschau
verfügbar. Installiere auf unterstützten Ubuntu- oder Debian-Distributionen ein `.deb`-Paket
oder unter Fedora ein `.rpm`-Paket. Pakete sind sowohl für x64-Prozessoren als auch
für ARM64-Prozessoren verfügbar.

Melde dich mit deinem ChatGPT-Konto an, um mit Projekten, lokalen Dateien und
Codex zu arbeiten. Einige Funktionen, darunter die Computernutzung, sind in der
Linux-Vorschau noch nicht verfügbar.

### Bestehendes Agenten-Setup und bisherige Arbeiten übernehmen

[Importiere Anweisungen, Einstellungen, Skills und Plug-ins sowie Projekte und aktuelle
Arbeiten](/codex/import) aus **Claude Code**, <strong>Claude Cowork</strong> oder
**Cursor** in die ChatGPT-Desktop-App. Aktiviere unter
**Einstellungen \> Import** automatische Updates, damit deine importierten Arbeiten synchron bleiben.

Nutze in Codex CLI `/import`, um unterstützte Bestandteile deines Setups und aktuelle Chats aus
Claude Code oder Cursor in deine lokale Sitzung zu übernehmen.

[Lies die Versionshinweise für Desktop und CLI
vom 11. August](/codex/changelog#codex-2026-08-11-app).

### Den passenden Zugang für defensive Sicherheitsaufgaben wählen

Daybreak bietet jetzt zwei Zugangsstufen für zugelassene Fachleute in der Cyberabwehr. **Daybreak Blue** unterstützt
allgemeine Abwehraufgaben wie die Sicherheitsprüfung von Code, die Reaktion auf Sicherheitsvorfälle und
die Validierung von Patches. **Daybreak Red** erfordert eine gesonderte Genehmigung und bietet
Zugang zu speziell trainierten Modellen für autorisierte Sicherheitsprüfungen.

Der Zugang setzt [Trusted Access for
Cyber](/de-DE/codex/cyber-safety#trusted-access-for-cyber) voraus und gilt ausschließlich für die
genehmigte Identität, den genehmigten Workspace oder die genehmigte Organisation, das genehmigte Modell und die genehmigte Produktoberfläche.

[Lies die Ankündigung zu Daybreak
vom 10. August](/codex/changelog#codex-2026-08-10-daybreak).

## 3.–7. August 2026

### Dateien und Projekte mit dem ChatGPT Sprachchat besprechen

Der [ChatGPT Sprachchat](/de-DE/codex/features/voice) unterstützt jetzt hochgeladene Dateien und
[ChatGPT-Projekte](/de-DE/codex/projects). Stelle während einer Sprachunterhaltung Fragen zu einem Dokument
oder setze ein Projekt anhand seiner letzten Chats, Quellen und
Anweisungen fort.

### Mit speziellen Plug-ins für den Bildungsbereich lernen und lehren

Drei neue [Plug-ins](/de-DE/codex/plugins) ermöglichen auf den Unterricht zugeschnittene Arbeitsabläufe in
ChatGPT Work und Codex. **College Student** erstellt Lernleitfäden,
Übungsquizze, Karteikarten und interaktive Erklärungen. **College Educator** hilft
bei der Entwicklung von Kursplänen, Materialien und Leistungsüberprüfungen. **K–12 Educator** unterstützt
die Unterrichtsplanung, die Erstellung von Unterrichtsmaterialien und deren Anpassung an unterschiedliche
Lernende.

Die Plug-ins sind über ChatGPT Edu und über schulbezirksweite Bereitstellungen von
ChatGPT for Teachers verfügbar. Schulen legen fest, welche Tools und Berechtigungen verfügbar sind. Lies
die [Ankündigung zu Plug-ins
für den Bildungsbereich](https://openai.com/index/learn-teach-chatgpt-work-codex/).

### Gespeicherte Dateien wiederverwenden und frühere Arbeit schneller finden

Im Web kannst du eine gespeicherte Datei aus der Bibliothek zu einem Gespräch hinzufügen, ohne sie erneut hochzuladen.
Außerdem kannst du die Bibliothek durchsuchen und formatierten Text einfügen, ohne Überschriften,
Links oder Listen zu verlieren. Die Suche findet im Web sowie unter iOS und Android auch
Ordner und Gesprächstitel.

Wenn du Text mit mehr als 10.000 Zeichen einfügst, wird er jetzt in allen ChatGPT-Tarifen
zu einem Anhang, auch in Enterprise und Edu. Wähle **Im Textfeld anzeigen** , wenn du
den Inhalt wieder in deine Nachricht übernehmen möchtest.

Lies die [Versionshinweise
zu ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes).

### Dein verbleibendes Nutzungskontingent für ChatGPT Work anzeigen

Berechtigte Personen mit persönlichen Tarifen oder ChatGPT Business können ihr verbleibendes
Nutzungskontingent für ChatGPT Work direkt in der Seitenleiste im Web prüfen. Welche Optionen für Credits verfügbar sind,
hängt von deinem Konto und deinen Berechtigungen im Workspace ab. ChatGPT Work und Codex
teilen sich weiterhin dieselben [Nutzungslimits und Credits](/de-DE/codex/pricing).

### Festlegen, wie GPT-5.6 in ChatGPT antwortet

Mit ChatGPT Plus oder Pro kannst du den Reasoning-Aufwand von GPT-5.6 Sol für eine
Antwort über einen neuen Schieberegler einstellen. Das aktualisierte Modell liefert außerdem verlässlichere Fakten
und gezieltere Antworten. GPT-5.6 Luna wird in den Tarifen Free
und Go zum Standardmodell von ChatGPT.

Diese Änderungen gelten für Gespräche in ChatGPT. Das Modellverhalten
in ChatGPT Work und Codex bleibt unverändert. Lies die [Versionshinweise
zu ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes).

### Arbeit organisieren und in Codex CLI 0.147.0 zwischen Agenten wechseln

[Codex CLI 0.147.0](https://github.com/openai/codex/releases/tag/rust-v0.147.0)
ergänzt dauerhaft gespeicherte, manuell sortierbare Chat-Bereiche und portable Agenten-Plug-ins.
Durchsuche lokale, persönliche, Workspace- und Remote-Kataloge für Plug-ins oder
[importiere dein Setup aus Cursor und Claude Code](/de-DE/codex/import), ohne synchronisierte
Gespräche zu duplizieren.

Verwende `--approve-for-me`, um die [automatische Überprüfung
von Genehmigungsanfragen](/de-DE/codex/sandboxing/auto-review) für geeignete Anfragen zu aktivieren, ohne
die Dateisystem- oder Netzwerkberechtigungen zu erweitern. Sitzungen mit Amazon Bedrock unterstützen außerdem
Websuche mit Cache und die Remote-Compaction (Kontextverdichtung) von Gesprächen.

### Umfassendere Sicherheitsscans verfolgen und fortsetzen

Die Versionen `0.1.16` bis `0.1.18` des gehosteten Codex-Security-Plugins bieten eine Live-Anzeige des Scan-Fortschritts,
den gemessenen Tokenverbrauch, fortsetzbare Tiefenscans und konfigurierbare
Limits für die Schwachstellensuche. Die neueste Version unterstützt außerdem die Authentifizierung über Amazon Bedrock
für Repository-Scans und die damit beauftragten Worker.

Nutze den [Arbeitsbereich von Codex Security](/de-DE/codex/security/plugin/workbench), um
Scan-Fortschritt und Befunde zu überprüfen, oder [konfiguriere einen
Tiefenscan](/de-DE/codex/security/plugin/deep-scans), wenn du eine gründlichere
Untersuchung benötigst. Sieh im [Änderungsprotokoll des Plug-ins](/de-DE/codex/security/plugin/changelog) nach,
welche Funktionen deine installierte Version unterstützt.

### Pull Requests auf GitHub auf Sicherheitsrisiken prüfen

[Codex Security Review](/de-DE/codex/security/security-review) analysiert Änderungen in Pull Requests
unter Berücksichtigung des Repository-Kontexts, von Bedrohungsmodellen und Sicherheitsleitlinien.
Richte automatische Reviews ein, die beim Öffnen eines Pull Requests oder bei neuen
Commits erfolgen, oder fordere ein Review direkt mit `@codex security review` an.

Die Funktion ist als Forschungsvorschau für berechtigte Personen mit ChatGPT Enterprise,
Business, Edu oder Pro verfügbar. In Plus ist sie nicht verfügbar, und es können
Nutzungslimits gelten.

## 27.–31. Juli 2026

### GPT-5.6 Terra und Luna zu niedrigeren Preisen nutzen

GPT-5.6 Terra kostet jetzt 20 % weniger und GPT-5.6 Luna 80 % weniger. Die Preise für Eingaben,
zwischengespeicherte Eingaben und Ausgaben wurden im selben Verhältnis gesenkt. Durch die aktualisierten
[Nutzungslimits und Preise](/de-DE/codex/pricing) eignet sich Terra noch besser für alltägliche
Aufgaben, während Luna besonders für gezieltes Programmieren und die Bearbeitung großer Aufgabenmengen geeignet ist.

### Hilfreichen Kontext im Browser und in geöffneten Tabs finden

In der ChatGPT-Desktop-App kann der [integrierte Browser](/de-DE/codex/browser)
Seiten aus deinem Browserverlauf finden oder direkt über seine Adressleiste bei Google suchen.
ChatGPT kann deinen Browserverlauf auch durchsuchen, wenn eine Aufgabe
früheren Kontext benötigt.

Mit der [Chrome-Erweiterung](/de-DE/codex/chrome-extension) kannst du offene Tabs erwähnen,
markierten Seitentext in einen Seitenchat übernehmen, Fragen zu YouTube-Videos stellen
oder im Kontextmenü einer Seite **ChatGPT fragen** auswählen. Prüfe und genehmige
Anfragen zur Nutzung des Browserverlaufs, bevor ChatGPT diese Informationen
in eine Aufgabe einbezieht.

### Änderungen in mehreren Repositorys überprüfen

Wenn ein [lokales Projekt mehr als einen
Ordner enthält](/de-DE/codex/projects#use-local-projects-for-folders-and-codebases), zeigt die Desktop-App
jedes Repository und die jeweils geänderten Zeilen an. Wähle
**Review** , um die Diffs gemeinsam zu prüfen, ohne zwischen verschiedenen
Review-Ansichten wechseln zu müssen.

### Generierte Bilder in deiner Unterhaltung verfeinern

Öffne ein generiertes Bild in der erweiterten Bildansicht und wechsle dann zwischen
**Fokussierte Ansicht** und **Canvas-Ansicht**. Füge Kommentare zu mehreren Bildern hinzu, wähle die
Versionen aus, die du behalten möchtest, und bitte um gezielte Änderungen, ohne den Chat zu verlassen.
Erfahre mehr über die [Bildgenerierung](/de-DE/codex/image-generation).

### Chats finden, die deine Aufmerksamkeit brauchen

Die neue **Aktivitätsansicht** der Desktop-App bündelt Chats, in denen du kürzlich
aktiv warst, und Aufgaben, die deine Aufmerksamkeit brauchen. Wähle die Glocke in der Seitenleiste,
um die Ansicht zu öffnen.

[Lies die Versionshinweise zur Desktop-App
vom 30. Juli](/codex/changelog#codex-2026-07-30-app).

### Partner-Tools über „Mit ChatGPT anmelden“ verbinden

**Mit ChatGPT anmelden** wird schrittweise als Beta für unterstützte Plug-ins und
Partner-Websites eingeführt, zunächst für Airtable, GitLab, HubSpot, Notion, Supabase und
Vercel. Damit kannst du in weniger Schritten ein Konto beim jeweiligen Partner erstellen oder verknüpfen und anschließend
den Dienst in ChatGPT oder Codex nutzen.

Partner erhalten nur deinen Namen, deine E-Mail-Adresse und, sofern vorhanden,
dein Profilbild. Der von jedem Plug-in angeforderte Zugriff muss weiterhin separat überprüft
und genehmigt werden. Lies die [Ankündigung zur Anmeldung
vom 29. Juli](/codex/changelog#codex-2026-07-29).

### In einem eigenen Workspace für die akademische Forschung zusammenarbeiten

[ChatGPT for Academic Researchers](https://openai.com/index/chatgpt-for-academic-researchers/)
bietet Hochschullehrenden und Postdocs, die die Teilnahmevoraussetzungen erfüllen, 12 Monate kostenlosen
Zugang zu einem eigenen ChatGPT-Workspace. Zugelassene Teams können bis zu fünf
verifizierte Forschende derselben Einrichtung umfassen. Für sie gelten die Datenschutzstandards für Unternehmen
und Nutzungslimits auf dem Niveau von ChatGPT Pro. Teilnehmende können GPT-5.6
in ChatGPT, ChatGPT Work und Codex für Forschungs- und Programmierabläufe nutzen.

Das Programm umfasst den Zugang zu ChatGPT, aber keine Credits für die OpenAI API. Voraussetzung für die Teilnahme sind
[eine Verifizierung der Zugehörigkeit zur Einrichtung und eine Forschungsarbeit,
die die Anforderungen erfüllt](https://help.openai.com/en/articles/20001406).

### Codex-Aufgaben unter iOS zuverlässiger fortsetzen

ChatGPT für iOS 1.2026.202 stellt die Verbindung zu Aufgaben zuverlässiger wieder her, wenn du zur
App zurückkehrst oder dein Gerät mit Face ID entsperrst. Sprachunterhaltungen verwenden die von dir gewählte
ChatGPT-Stimme und zeigen Warnungen zu Nutzungslimits an. Der Editor schlägt jetzt wie in der Desktop-App
installierte Plug-ins und ihre Skills vor.

Die Version verbessert außerdem die Bedienelemente zum Pausieren und Fortsetzen von Zielen, Inline-Tabellen
und Designs, große Workspace-Diffs, Verweise auf markierten Text sowie die Wiederherstellung
der Modellauswahl. Lies die [Versionshinweise für iOS
vom 27. Juli](/codex/changelog#codex-2026-07-27-mobile).

### Sicherheitsscans vergleichen und Befunde verwalten

Die Versionen `0.1.14` und `0.1.15` des gehosteten Codex-Security-Plugins bieten Scanvergleiche,
Feedback zu Fehlalarmen, `SECURITY.md`-Richtlinien mit festgelegtem Geltungsbereich sowie übersichtlichere Verläufe für Repositorys
und Befunde. Du kannst Befunde auswählen, um sie in Linear oder GitHub-Issues nachzuverfolgen.
Codex überprüft dabei die vorgeschlagene Aktion, bevor du sie genehmigst.

Verwende den vorhandenen [Arbeitsbereich für
Codex Security](/de-DE/codex/security/plugin/workbench), um gespeicherte Scans, Befunde,
den Repository-Verlauf und die Behebung von Problemen in der Desktop-App zu prüfen. Der Katalog für gehostete Plug-ins
bietet Version `0.1.15`, der öffentliche Marketplace für CLI-Plug-ins
dagegen Version `0.1.11`. Lies das [Änderungsprotokoll
des Codex-Security-Plugins](/de-DE/codex/security/plugin/changelog), bevor du dich auf eine neue Funktion verlässt.

### Sicherheitsscans über das Terminal, CI oder TypeScript ausführen

Die öffentliche CLI und das TypeScript SDK von `@openai/codex-security` sind jetzt in Version
`0.1.5` verfügbar. Ihre Versionsnummern sind unabhängig von denen des Codex-Security-Plugins. Mit dem
Paket kannst du [Scans über die CLI ausführen](/de-DE/codex/security/cli), Änderungen in Pull Requests
überprüfen und SARIF-Ergebnisse in [CI](/de-DE/codex/security/cli/ci) hochladen oder
fortsetzbare [Sammelscans](/de-DE/codex/security/cli/bulk-scans) über mehrere GitHub-Repositorys hinweg
oder anhand einer festgeschriebenen CSV-Inventarliste ausführen.

Mit dem [Codex Security TypeScript SDK](/de-DE/codex/security/sdk) kannst du außerdem
Scans, Fortschrittsmeldungen, Kostenkontrollen und Abbruchfunktionen in deine eigenen
Tools integrieren. Das Paket ist öffentlich, für Scans ist aber weiterhin Zugriff auf Codex Security
erforderlich. Einige Scans ganzer Repositorys setzen zusätzlich Trusted Access for Cyber voraus.

### Sitzungen organisieren und Codex CLI 0.146.0 erweitern

Mit [Codex CLI 0.146.0](https://github.com/openai/codex/releases/tag/rust-v0.146.0)
kannst du einen neuen Chat mit `/new release prep` oder `/clear bug bash` benennen,
wichtige Threads anpinnen und zwischen Nebenunterhaltungen wechseln, ohne sie zu schließen.
Hinzu kommen temporäre Forks von Unterhaltungen, eine eigenständige Websuche für kompatible
benutzerdefinierte Modellanbieter, vom Executor bereitgestellte Skills sowie Unterstützung für Manifeste von Agenten-Plug-ins,
die Veröffentlichung von Plug-ins im Workspace und weitere Plug-in-Marketplaces.

Für eigene Clients kann der [App Server](/de-DE/codex/app-server) angepinnte Threads filtern,
Forks im Arbeitsspeicher erstellen, den Status installierter Konnektoren prüfen und
deren Metadaten lesen. Die experimentelle WebSocket-Unterstützung verbindet app-server außerdem mit
entfernten Hosts für Code Mode. Prüfe die
[Sicherheitsanforderungen für den App Server](/de-DE/codex/app-server#connect-the-cli-terminal-ui),
bevor du eine Remote-Verbindung zugänglich machst. Die Version verbessert außerdem die Proxy-Unterstützung,
die Wiederverbindung mit MCP, die Reaktionsfähigkeit des Terminals und die Zuverlässigkeit der Windows-Sandbox.

### GPT-5.6 Sol für gehostete Codex-Aufgaben nutzen

[GPT-5.6 Sol](/de-DE/codex/models#recommended-models) übernimmt jetzt Code Review
und Qualitätssicherung in Codex Cloud für berechtigte Kundinnen und Kunden. Sol ist das Flagship-Modell
der GPT-5.6-Familie für komplexe Programmieraufgaben, Recherche, Computernutzung und Sicherheitsaufgaben.
Codex Cloud wählt sein Modell automatisch aus. Terra und Luna bleiben auf
unterstützten lokalen Oberflächen und Weboberflächen verfügbar.

### Auf die Einstellung der GPT-5.4-Modelle vorbereiten

Ab dem 31. August sind GPT-5.4 und GPT-5.4 mini in Codex für alle, die sich
mit ChatGPT anmelden, nicht mehr verfügbar. Ersetze `gpt-5.4` durch `gpt-5.6-terra` und `gpt-5.4-mini`
durch `gpt-5.6-luna` in den Standardeinstellungen des Workspaces, gespeicherten Modelleinstellungen,
verwalteten Konfigurationen, benutzerdefinierten Agenten und geplanten Aufgaben.

Die OpenAI API und Codex-Sitzungen, die mit einem API-Schlüssel authentifiziert sind, bleiben
davon unberührt. Prüfe die [abgekündigten Codex-Modelle](/de-DE/codex/models#deprecated-codex-models)
und die [Modellverfügbarkeit
im Workspace](/de-DE/codex/enterprise/workspace-model-availability) vor dem
Stichtag.

## 20.–24. Juli 2026

### Aufgaben mit dem ChatGPT Sprachchat besprechen

Mit dem [ChatGPT Sprachchat](/de-DE/codex/features/voice) auf Basis von GPT-Live kannst du Aufgaben
besprechen und sie in Chat, Work und Codex in der ChatGPT-Desktop-App koordinieren.
Starte einen neuen Chat oder eine neue Aufgabe im Sprachmodus und bitte ChatGPT dann, Aufgaben in anderen Threads zu starten,
zu prüfen oder zu steuern.

Sage unter macOS „Schau dir das an“, um einen [Appshot](/de-DE/codex/appshots) deines
vordersten Fensters zu teilen, wenn **Bildschirmkontext** aktiviert ist.

Der Sprachchat ist mit den Tarifen Plus, Pro, Business, Edu und Enterprise in der
Desktop-App und über [Remote unter iOS](/de-DE/codex/remote-connections#set-up-mobile-access) verfügbar.

### In einem lokalen Projekt mit mehreren Ordnern arbeiten

Lokale Projekte in der ChatGPT-Desktop-App können jetzt mehrere zusammengehörige
Ordner umfassen. Wähle einen primären Ordner für neue Chats, Git-Vorgänge und die automatische
Erkennung von `AGENTS.md`, Skills und `config.toml`. Sekundäre Ordner stehen weiterhin
zum Suchen, Lesen und Bearbeiten von Dateien zur Verfügung.

Öffne **Projekt bearbeiten** , um [Ordner hinzuzufügen und den primären
Ordner auszuwählen](/de-DE/codex/projects#use-local-projects-for-folders-and-codebases).

[Lies die Versionshinweise vom 23. Juli](/codex/changelog#codex-2026-07-23-app).

## 13.–17. Juli 2026

### Work-Unterhaltungen und Projekte auf dem Desktop bündeln

Die ChatGPT-Desktop-App zeigt Chat- und Work-Unterhaltungen jetzt gemeinsam in der
ChatGPT-Ansicht. Work-Unterhaltungen in der Cloud werden zwischen Web, Mobilgeräten und Desktop synchronisiert;
lokale Work-Unterhaltungen bleiben auf deinem Computer. ChatGPT-Projekte sind
in der Desktop-App verfügbar. Codex behält seine eigene Ansicht und einen separaten Verlauf für
Entwicklungsabläufe.

[Vergleiche ChatGPT Work und Codex auf dem
Desktop](/de-DE/codex/use-chatgpt#compare-chatgpt-work-and-codex-on-desktop), um die
passende Ansicht für deine Aufgabe auszuwählen.

### Parallele Arbeit in Codex mit Codex Micro steuern

Am 15. Juli brachten OpenAI und Work Louder
[Codex Micro](/de-DE/codex/features/codex-micro) auf den Markt, ein in begrenzter Stückzahl produziertes Bediengerät
für Codex in der ChatGPT-Desktop-App. Seine Agententasten zeigen den Status von
bis zu sechs Chats an und ermöglichen den Wechsel zwischen ihnen. Mit anpassbaren Befehlstasten,
einem Analogstick und einem Drehregler kannst du häufige Aktionen oder Skills auslösen, Push-to-Talk starten und
den Reasoning-Aufwand anpassen, ohne die Hände von der Tastatur zu nehmen.

### GPT-5.6 über Amazon Bedrock nutzen

GPT-5.6 Sol, Terra und Luna sind jetzt über Amazon Bedrock allgemein verfügbar.
Lokale Oberflächen von ChatGPT Work und Codex können den integrierten
[Provider `amazon-bedrock`](/de-DE/codex/amazon-bedrock) mit einem Bedrock-API-Schlüssel oder der
Anmeldeinformationskette des AWS SDK nutzen. Dazu zählen Work und Codex in der ChatGPT-Desktop-App,
Codex CLI, die IDE-Erweiterung und das Codex SDK.

### Visualisierungen von Codex-Aufgaben unter iOS ansehen

ChatGPT für iOS 1.2026.188 hat Inline-Visualisierungen für Codex-Aufgaben eingeführt und
das Erstellen und Verwalten von Aufgaben aus Unterhaltungen heraus verbessert. Dazu gehören zuverlässige
Links zu neu erstellten Aufgaben. Lies die
[Versionshinweise für iOS vom 13. Juli](/codex/changelog#codex-2026-07-13-mobile).

## 6.–10. Juli 2026

<a id="take-on-ambitious-work-with-chatgpt-work"></a>

### Anspruchsvolle Aufgaben in ChatGPT angehen

Mit [ChatGPT Work](/de-DE/codex/get-started-with-work) kann ChatGPT Kontext aus
deinen Dateien und [Plug-ins](/de-DE/codex/plugins) zusammentragen,
Aktionen in verschiedenen Arbeitsabläufen ausführen und Dokumente, Präsentationen,
Tabellen, Sites und andere fertige Arbeitsergebnisse zur Überprüfung erstellen. Auf Basis von
[GPT-5.6](/de-DE/codex/models) kann es ein Ziel in Schritte aufteilen und stundenlang arbeiten, während
du den Fortschritt verfolgst, Fragen beantwortest, die Richtung änderst und
wichtige Aktionen genehmigst.

[Geplante Aufgaben](/de-DE/codex/automations) können die Arbeit auch in deiner Abwesenheit voranbringen.
Sie können einmalig, nach einem Zeitplan, beim Eintreten eines Ereignisses oder während der laufenden
Überwachung von Änderungen ausgeführt werden.

### Das passende GPT-5.6-Modell auswählen

Die [GPT-5.6-Familie](/de-DE/codex/models#recommended-models) bietet drei empfohlene
Modelle für ChatGPT Work, die ChatGPT-Desktop-App, Codex CLI und die Codex IDE-Erweiterung.
Sol ist das Flagship-Modell für komplexe Programmieraufgaben, Computernutzung, Recherche und
Sicherheitsaufgaben. Terra bietet ein ausgewogenes Verhältnis von Leistung und Kosten für die tägliche Arbeit, während Luna
die schnellste und kostengünstigste Option ist. Die Standardeinstellung **Leistung** nutzt Sol mit
mittlerem Reasoning-Aufwand.

### Codex in der ChatGPT-Desktop-App nutzen

Am 9. Juli wurde die Codex App in die
[ChatGPT-Desktop-App](/de-DE/codex/app) für macOS und Windows integriert. Codex behält seinen
eigenen Programmierbereich neben Chat und Work in ChatGPT. Zu den Codex-Funktionen gehören
Inline-Bearbeitung in Diffs, die Überprüfung von Pull Requests im Seitenbereich, schnellere
[Computernutzung](/de-DE/codex/computer-use) auf Basis von GPT-5.6 sowie Projekte
mit mehreren Repositorys.

Wenn du die Codex App bereits nutzt, kannst du sie wie gewohnt aktualisieren. Du kannst Codex als Standardansicht
festlegen, das Codex-Logo als App-Symbol verwenden und über die mobile ChatGPT-App auf Codex-Projekte
auf deinem Desktop zugreifen. Die aktualisierte Desktop-App ist weltweit mit jedem
ChatGPT-Tarif verfügbar, auch mit Free.

## 15.–19. Juni 2026

### Vorgeführte Arbeitsabläufe in wiederverwendbare Skills umwandeln

Mit [Aufzeichnen und Wiedergeben](/de-DE/codex/extend/record-and-replay) kannst du ChatGPT oder
Codex unter macOS einen Arbeitsablauf zeigen und daraus einen wiederverwendbaren Skill erstellen lassen. Nutze
die Funktion für wiederkehrende Aufgaben, die sich leichter zeigen als beschreiben lassen. Verfeinere anschließend den
generierten Skill und führe ihn mit neuen Eingaben erneut aus. Die Funktion ist zunächst nicht
im EWR, im Vereinigten Königreich oder in der Schweiz verfügbar und setzt Computernutzung voraus.

<a id="continue-a-task-on-another-host"></a>

### Einen Chat auf einem anderen Host fortsetzen

Mit der [Chat-Übergabe](/de-DE/codex/remote-connections#hand-off-a-chat-between-hosts)
verschiebst du einen Chat samt Git-Zustand zwischen deinem lokalen Computer und einem verbundenen
Remote-Host. Codex kann am Ziel einen Worktree erstellen oder wiederverwenden, den Chat
übertragen und im passenden Projekt weiterarbeiten.

Dasselbe Desktop-Update ergänzt den Verlauf geplanter Ausführungen um Sammelaktionen. So
kannst du alle Ausführungen als gelesen markieren oder archivierbare Ausführungen gemeinsam archivieren.

### Workspaces unter iOS durchsuchen und überprüfen

In der mobilen ChatGPT-App unter iOS bietet **Remote** jetzt einen Dateibrowser für den Workspace,
eine Verzeichnisauswahl für neue Chats, Bedienelemente zum Ein- und Ausklappen von Diffs sowie
Optionen für MCP-Genehmigungen pro Chat oder chatübergreifend.

Auch die Einführung von Computernutzung, der Chrome-Erweiterung, Erinnerungen und Chronicle
im EWR, im Vereinigten Königreich und in der Schweiz hat begonnen. Erinnerungen bleiben
in diesen Regionen standardmäßig deaktiviert. Chronicle ist eine Forschungsvorschau
für Personen mit einem ChatGPT Pro-Abonnement unter macOS und muss ausdrücklich aktiviert werden.

Lies die Versionshinweise [für iOS vom 15. Juni](/codex/changelog#codex-2026-06-15-mobile),
[zur Verfügbarkeit vom 16. Juni](/codex/changelog#codex-2026-06-16-app) und
[zur App vom 18. Juni](/codex/changelog#codex-2026-06-18-app).

## 8.–12. Juni 2026

### Web-Apps mit dem Entwicklermodus des Browsers debuggen

Der [Entwicklermodus](/de-DE/codex/browser?surface=app#app-developer-mode) gibt Codex kontrollierten
Zugriff auf Funktionen des Chrome DevTools Protocol in Chrome und im integrierten
Browser. Codex kann Netzwerkverkehr, Konsolenausgaben, Laufzeitfehler und
den Seitenzustand untersuchen, während es die Leistung deiner App analysiert oder Fehler darin sucht. Aktiviere unter **Entwicklermodus** in
**Einstellungen** \> **Browser** die Option **Vollständigen CDP-Zugriff aktivieren**. Codex fordert eine
ausdrückliche Genehmigung an, bevor es diesen Zugriff auf einer Website nutzt.

Auch die Browsernutzung ist bis zu doppelt so schnell: Durch Optimierungen an CDP und DOM-Snapshots
sind weniger Anfrage-Antwort-Zyklen mit dem Browser nötig.

  
    
  

### Dein Setup in Codex übernehmen

Neue Migrationsabläufe können beim Einstieg unterstützte Bestandteile des Setups anderer Programmieragenten
importieren. Die Codex App unterstützt jetzt außerdem `/init` zum Erstellen von Projektanweisungen.
Zusätzlich wurden die Plug-in-Verwaltung, die Browserdiagnose und die Zusammenfassungen
abgeschlossener Chats verbessert.

<a id="set-up-codex-tasks-from-ios"></a>

### Codex-Chats unter iOS einrichten

Mit Remote unter iOS kannst du jetzt einen Branch auswählen, einen Worktree erstellen, ein Setup-Skript für die Umgebung
ausführen, Ziele verwalten und Inline-Review-Kommentare hinzufügen.

Lies die Versionshinweise [zur App vom 9. Juni](/codex/changelog#codex-2026-06-09-app),
[für iOS vom 9. Juni](/codex/changelog#codex-2026-06-09-mobile) und
[zur App vom 11. Juni](/codex/changelog#codex-2026-06-11-app).

## 1.–5. Juni 2026

### Erstelle und veröffentliche Websites mit Sites

Mit [Sites](/de-DE/codex/sites) kann ChatGPT Websites, Dashboards, interne Tools, Web-Apps und Spiele
erstellen, speichern, bereitstellen und überprüfen. OpenAI übernimmt das Hosting. Sites hat
einen eigenen Zugang in ChatGPT im Web und in der Desktop-App. Dort kannst du
zu deinen Projekten zurückkehren und Werte sowie Secrets der gehosteten Umgebung verwalten,
ohne einen separaten Deployment-Stack zusammenstellen zu müssen.

### Nutze Codex mit Amazon Bedrock

Du kannst [Codex mit Amazon Bedrock nutzen](/de-DE/codex/amazon-bedrock), um lokale
Arbeitsabläufe mit von AWS verwalteter Authentifizierung, Kontoverwaltung und Abrechnung auszuführen.
Remote unter iOS bietet jetzt außerdem eine optionale App-Sperre, Einstellungen zum Verhalten bei Folgeanfragen,
Zeilenumbrüche für Diffs und SSH-Verbindungen zu Windows-Rechnern. In der Desktop-App
kannst du nun die Position des Terminals festlegen und in der Profilansicht
Informationen zu deinen Aktivitäten einsehen.

[Lies alle Versionshinweise vom Juni 2026](/codex/changelog#month-2026-06).

## 25.–29. Mai 2026

### Nutze Windows-Apps und steuere Codex aus der Ferne

Mit der [Computernutzung](/de-DE/codex/computer-use#windows-foreground-use) kann Codex nun
Inhalte von Windows-Desktop-Apps sehen, darin klicken und Text eingeben. Installiere vor dem Start
das Plug-in für Computernutzung. Unter Windows nutzt Codex den aktiven Desktop und übernimmt
während der Aufgabe die Steuerung im Vordergrund. Remote-Verbindungen unterstützen ebenfalls
Windows. Öffne in der mobilen ChatGPT-App **Remote** , um auf einem Windows-Gerät
zu arbeiten, oder nutze einen Mac mit der ChatGPT-Desktop-App und verfolge den Fortschritt
von einem anderen Ort aus.

Remote unter iOS unterstützt jetzt auch den Einstieg über Spotlight und Kurzbefehle, das Durchsehen
archivierter Chats, `/side` sowie das Speichern oder Kopieren gerenderter Bilder. Die Desktop-App
bietet nun eine Chat-Koordination für lokale Projekte und Worktrees, eine Suche nach Inhalten und
Branch-Namen in früheren Chats sowie einheitliche visuelle Kennzeichnungen für
Subagenten im Hintergrund.

Lies die Versionshinweise [für iOS vom 25. Mai](/codex/changelog#codex-2026-05-25-mobile) und
[für die App vom 29. Mai](/codex/changelog#codex-2026-05-28-app).

## 18.–22. Mai 2026

### Gib Codex mit Appshots Kontext aus jeder Mac-App

Mit [Appshots](/de-DE/codex/appshots) sendest du einen Screenshot des vordersten App-Fensters und den verfügbaren Text an Codex,
indem du beide Command-Tasten drückst. So erhält Codex
Kontext für seine Arbeit aus Designtools, Dashboards, Dokumenten und anderen Apps,
ohne dass du Bildschirminhalte kopieren, einfügen oder beschreiben musst.

### Verfolge Ziele über längere Zeit

Der [Zielmodus](/de-DE/codex/prompting#goal-mode) ist nicht mehr experimentell und steht
in der Codex App, der IDE-Erweiterung und der CLI für Ziele bereit, deren Umsetzung
Stunden oder Tage dauern kann. Mit der [Nutzung im gesperrten Zustand](/de-DE/codex/computer-use#locked-use) kann Codex
genehmigte Aufgaben mit Computernutzung fortsetzen, nachdem ein Mac gesperrt wurde, auch über
**Remote** in der mobilen ChatGPT-App. In ChatGPT Business-Workspaces lassen sich außerdem
[wiederverwendbare Plug-in-Pakete mit Workspace-Mitgliedern teilen](https://developers.openai.com/plugins/build/plugins#share-a-local-plugin-with-your-workspace).

[Lies die Hinweise zur Veröffentlichung vom 21. Mai](/codex/changelog#codex-2026-05-21).

## 11.–15. Mai 2026

### Setze deine Desktop-Arbeit auf dem Smartphone fort

In der mobilen ChatGPT-App verbindet dich **Remote** mit einem Mac, auf dem die
ChatGPT-Desktop-App läuft. Da die Arbeit auf dem verbundenen Host ausgeführt wird, bleiben deine Projekte, Dateien,
Zugangsdaten, Skills und Plug-ins sowie deine Konfiguration verfügbar, wenn du
auf dem Smartphone weiterarbeitest. Unter [Remote-Verbindungen](/de-DE/codex/remote-connections) erfährst du,
wie du einen Host einrichtest und die Arbeit auf einem anderen Gerät fortsetzt.

### Automatisiere vertrauenswürdige Arbeitsabläufe

Hooks sind jetzt allgemein verfügbar, um benutzerdefinierte Befehle an wichtigen Punkten
im Lebenszyklus des Agenten auszuführen. Admins von ChatGPT Enterprise können außerdem
[Codex-Zugriffstoken](/de-DE/codex/enterprise/access-tokens) für vertrauenswürdige Skripte,
Scheduler und private CI-Runner aktivieren. Die Dokumentation für Unternehmen wurde um Hinweise
zum verwalteten Setup und zu Steuerungsmöglichkeiten für Codex erweitert.

[Lies die Hinweise zur Veröffentlichung vom 14. Mai](/codex/changelog#codex-2026-05-13-app).

## 4.–8. Mai 2026

### Arbeite mit der Chrome-Erweiterung über mehrere Browser-Tabs hinweg

Die [Chrome-Erweiterung](/de-DE/codex/chrome-extension) kann im Hintergrund
parallel in mehreren Tabs arbeiten, ohne deinen Browser zu übernehmen. Du
bestimmst, welche Websites Codex nutzen darf. So kannst du Recherche,
Dateneingabe und Überprüfung über mehrere Web-Apps hinweg in einer Aufgabe verbinden.

Die Codex App bietet jetzt auch die Bereinigung diktierter Texte sowie ein benutzerdefiniertes Wörterbuch für Namen,
Dateipfade und Codesymbole. Mit der Inhaberrolle in einem ChatGPT Enterprise-Workspace kannst du
Mitgliedern erlauben, [Codex-Zugriffstoken](/de-DE/codex/enterprise/access-tokens) für
vertrauenswürdige, nicht interaktive lokale Arbeitsabläufe zu erstellen.

Lies die Hinweise zur Veröffentlichung [der App vom 5. Mai](/codex/changelog#codex-2026-05-05-app),
[der Zugriffstoken vom 5. Mai](/codex/changelog#codex-2026-05-05) und
[von Codex für Chrome](/codex/changelog#codex-2026-05-07).

## 20.–24. April 2026

### Nutze GPT-5.5 für komplexe Aufgaben

[GPT-5.5](/de-DE/codex/models) wurde in Codex als empfohlenes Modell für die meisten
Aufgaben eingeführt. Seine Stärken liegen in Implementierung, Debugging, Tests, Computernutzung,
Recherche und der Ausarbeitung fertiger Ergebnisse bei wissensbasierten Aufgaben.

### Lass Codex den Browser bedienen und Genehmigungen überprüfen

Mit [Computernutzung im integrierten Browser](/de-DE/codex/browser?surface=app#app-computer-use-in-the-browser)
kann Codex sich durch Seiten lokaler Entwicklungsserver und dateibasierte Seiten klicken, um
Probleme zu reproduzieren und Fehlerbehebungen zu überprüfen. Geeignete Genehmigungsanfragen können außerdem
die [automatische Überprüfung von Genehmigungsanfragen](/de-DE/codex/sandboxing/auto-review) durchlaufen.
Dabei werden der Überprüfungsstatus und das Risiko angezeigt, bevor die Aktion ausgeführt wird.

[Lies die Hinweise zur Veröffentlichung vom 23. April](/codex/changelog#codex-2026-04-23).

## 13.–17. April 2026

### Vorschau und Bedienung an einem Ort

Im [integrierten Browser](/de-DE/codex/browser?surface=app) kamen Live-Vorschauen und Kommentare zu Seiten hinzu.
Mit [Computernutzung](/de-DE/codex/computer-use) konnte Codex macOS-Apps sehen und
bedienen. Zusammen ermöglichten diese Funktionen, die visuelle Umsetzung und die End-to-End-Prüfung
im Rahmen derselben Aufgabe wie die Codeänderung zu erledigen.

  
    
  

<a id="start-with-a-task-and-keep-it-moving"></a>

### Starte mit einem Chat und setze die Arbeit fort

[Eigenständige Chats](/de-DE/codex/projects#start-without-a-project) ermöglichten den Einstieg,
ohne einen Projektordner auszuwählen. Dieselbe Version brachte
[geplante Aufgaben innerhalb eines Chats](/de-DE/codex/automations#schedule-a-task-inside-a-chat),
Kontext zu Pull Requests, erweiterte Dateivorschauen und [Erinnerungen](/de-DE/codex/customization/memories) für
die Arbeit über mehrere Chats hinweg.

[Lies die Versionshinweise zur Codex App vom 16. April](/codex/changelog#codex-2026-04-16-app).

## 6.–10. April 2026

### Prüfe und veröffentliche Pull Requests in der App

Für Reviews kamen einklappbare Inline-Kommentare, ein Inline-Modus, ein separater
Review-Modus und klarere Kontextinformationen zu Git und Quellcode hinzu. Aktivitäten und Kommentare
zu Pull Requests sowie Push-Optionen wurden dann ebenso wie Datei-Tabs für den Workspace in die App
integriert. So konntest du eine Änderung prüfen und darauf reagieren, ohne das Tool zu wechseln.

Lies die Versionshinweise zur Codex App vom [9. April](/codex/changelog#codex-2026-04-09-app) und
[10. April](/codex/changelog#codex-2026-04-10-app) oder erfahre,
wie du [Änderungen in der App überprüfst](/de-DE/codex/code-review?surface=app).

## 23.–27. März 2026

### Bündle Arbeitsabläufe als Plug-ins

[Plug-ins](/de-DE/codex/plugins) wurden als installierbare Pakete aus Skills,
Konnektoren und MCP-Servern eingeführt. Damit ließen sich vollständige Arbeitsabläufe leichter finden,
installieren und teilen. Neu gestaltete Seiten für Plug-ins und Skills zeigten deren Inhalte
und Status übersichtlicher an. In derselben Woche kam auch die Suche nach früheren Chats hinzu.

Lies die Versionshinweise zur [Aufgabensuche](/codex/changelog#codex-2026-03-24-app),
zur [Einführung von Plug-ins](/codex/changelog#codex-2026-03-25) und
zur [Codex App](/codex/changelog#codex-2026-03-25-app).

## 16.–20. März 2026

### Forke Chats ab früheren Nachrichten und wähle Tools im Editor

Du konntest einen Chat ab einer früheren Nachricht forken und so leichter einen neuen
Ansatz ausprobieren, ohne den ursprünglichen Verlauf zu verlieren. Befehle für das Modell und den Reasoning-Aufwand
standen bereits beim Verfassen zur Verfügung. Aktivierte Skills erschienen im `@`-Menü,
und GPT-5.4 mini bot eine schnellere Option für einfachere Aufgaben und Subagenten.

Lies die Versionshinweise zu [GPT-5.4 mini](/codex/changelog#codex-2026-03-17),
zur [Chat-Steuerung](/codex/changelog#codex-2026-03-18-app) und
zum [Skill-Menü](/codex/changelog#codex-2026-03-19-app).

## 9.–13. März 2026

### Plane Aufgaben in der passenden Umgebung

[Geplante Aufgaben](/de-DE/codex/automations) konnten lokal oder in einem Worktree
mit einem ausdrücklich festgelegten Modell und Reasoning-Aufwand laufen. Mit wiederverwendbaren Vorlagen ließen sich gängige
Aufgaben schneller konfigurieren, und benutzerdefinierte Designs erleichterten es,
den Workspace individuell anzupassen.

  
    
  

### Lass Codex Terminalausgaben prüfen

Codex konnte nun auch das [integrierte Terminal](/de-DE/codex/integrated-terminal#run-and-validate-your-project)
des aktuellen Chats auslesen. So konnte es einen laufenden Entwicklungsserver oder Build-Ausgaben
direkt prüfen, statt dich zu bitten, die Ausgaben einzufügen.

Lies die Versionshinweise zur Codex App vom [11. März](/codex/changelog#codex-2026-03-11-app) und
[12. März](/codex/changelog#codex-2026-03-12-app).

## 2.–6. März 2026

### Codex nativ unter Windows ausführen

Die Codex App erschien für [Windows](/de-DE/codex/windows/windows-app) mit nativer Unterstützung für PowerShell
und die Sandbox sowie mit Worktrees, geplanten Aufgaben und Skills. WSL blieb
für Entwickelnde verfügbar, die eine Linux-Umgebung bevorzugten.

  
    
  

<a id="move-tasks-between-local-and-worktree"></a>

### Chats zwischen Lokal und Worktree verschieben

Mit der [Übergabe zwischen Lokal und Worktree](/de-DE/codex/environments/git-worktrees#working-between-local-and-worktree)
ließ sich ein aktiver Chat verschieben, ohne seinen Kontext zu verlieren. In derselben Woche
erschien auch GPT-5.4 in Codex für Programmierung, Computernutzung und
Arbeitsabläufe mit längerem Kontext.

Lies die Versionshinweise zur [Veröffentlichung für Windows](/codex/changelog#codex-2026-03-04-app),
zur [Worktree-Übergabe](/codex/changelog#codex-2026-03-03-app) und
zu [GPT-5.4](/codex/changelog#codex-2026-03-05).

## 9.–13. Februar 2026

### In Echtzeit iterieren und Chats für neue Ansätze forken

GPT-5.3-Codex-Spark erschien als Forschungsvorschau. Das Modell reagierte nahezu sofort und ermöglichte es, Code in Echtzeit schrittweise weiterzuentwickeln.
In der App konntest du nun außerdem Chats forken und ein frei schwebendes Chatfenster nutzen, das immer im Vordergrund blieb.
So konntest du einen anderen Ansatz ausprobieren oder
Codex neben einem Editor oder Browser geöffnet lassen.

Lies die Versionshinweise zu [Spark](/codex/changelog#codex-2026-02-12) und zur
[Codex App](/codex/changelog#codex-2026-02-12-app) oder sieh dir den
aktuellen [Leitfaden zu den Modellen](/de-DE/codex/models) an.

## 2.–6. Februar 2026

### Die Codex App erscheint für macOS

Die Codex App erschien als Desktop-Workspace mit parallelen Projekt-Chats,
integriertem Git-Review, Worktrees, Skills, geplanten Aufgaben und Diktierfunktion.
Diese Funktionen sind heute in Codex in der [ChatGPT-Desktop-App](/de-DE/codex/app) verfügbar.

  
    
  

### Laufende Arbeit steuern und Dateien hinzufügen

Mit neuen Anweisungen während einer laufenden Antwort konntest du Codex neu ausrichten,
ohne die Antwort abzubrechen. Außerdem ließen sich nun auch andere Dateien als Bilder anhängen.
Diese Möglichkeiten bildeten die Grundlage dafür, [Codex zu steuern und weitere Nachrichten in die Warteschlange zu stellen](/de-DE/codex/prompting#steering-and-queuing)
und dabei den Kontext mitzugeben, den Codex benötigt.

Lies die [Hinweise zur Veröffentlichung der Codex App](/codex/changelog#codex-2026-02-02) und
die [Versionshinweise zur App vom 5. Februar](/codex/changelog#codex-2026-02-05-app).

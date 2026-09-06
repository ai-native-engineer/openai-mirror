<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/chatgpt-work-overview -->

ChatGPT Work und Codex nutzen dieselben grundlegenden Mechanismen für Ausführung, Isolierung und Berechtigungen. Für beide gelten dieselben Sicherheitsgrenzen, die Bestandteil deines Vertrags für ChatGPT Business oder Enterprise sind. Welche Funktionen und Steuerungsmöglichkeiten jeweils verfügbar sind, hängt davon ab, ob eine Aufgabe lokal oder in der Cloud ausgeführt wird, welche Tools ihr zur Verfügung stehen und welche Workspace-Richtlinien gelten.

ChatGPT Work kann mehrstufige Aufgaben mit den Informationen, Dateien, Anwendungen und Tools erledigen, die einem autorisierten Workspace-Mitglied zur Verfügung stehen. Im Web werden diese Aufgaben in der Cloud ausgeführt, nicht auf dem Gerät des Mitglieds.

Diese Übersicht erläutert die Grenzen der Ausführungsumgebung, Netzwerk- und Anwendungskontrollen, den Umgang mit Daten und die sichere Ausführung von Aufgaben mit ChatGPT Work im Web. Die Verfügbarkeit und die administrativen Steuerungsmöglichkeiten hängen von deinem Tarif und der Konfiguration deines Workspace ab.

Details zur gehosteten Ausführung, zu Berechtigungen verbundener Konten,
zu Browser- und Netzwerkeinstellungen, zur Aufbewahrung und zu den für Audits einsehbaren Informationen findest du unter
[Cloud-Sicherheit in ChatGPT Work](/de-DE/codex/enterprise/chatgpt-work-cloud-security).

Informationen zum Gerätezugriff, zu lokalen Browsersitzungen, verwalteten Richtlinien
und zum lokalen Umgang mit Daten findest du unter
[Lokale Sicherheit in ChatGPT Work](/de-DE/codex/enterprise/chatgpt-work-local-security).

## Isolierte Ausführung, Dateien und Gerätezugriff

Welche Dateien und Tools ChatGPT Work zur Verfügung stehen, hängt davon ab, wo Work ausgeführt wird, welche Berechtigungen Nutzende haben und wie die Administration Work konfiguriert hat.

### Work lokal

Bei lokaler Ausführung erledigt Work Aufgaben über die ChatGPT-Desktop-App auf deinem Gerät. Es kann auf lokale Dateien, Anwendungen und andere bereitgestellte Ressourcen zugreifen, sofern deine Berechtigungen, die geltenden Kontrollen im Workspace und die Sicherheitsrichtlinien des Geräts dies zulassen. Anders als Work im Web kann Work bei lokaler Ausführung mit Ressourcen arbeiten, die auf deinem Computer bleiben, ohne dass du Dateien in einen Cloud-Chat hochladen musst.

### Work in der Cloud

Work in der Cloud ist auf unterstützten Web-, Mobil- und Desktop-Oberflächen verfügbar. Dabei wird der Codex-Harness in einer isolierten Umgebung auf einer von OpenAI verwalteten Infrastruktur ausgeführt. Cloud-Chats können zwischen diesen Oberflächen synchronisiert werden. Unterstützte Aufgaben können weiterlaufen, auch wenn die jeweilige Person gerade nicht im Chat ist.

Work im Web kann nicht direkt auf Dateien, Anwendungen oder geöffnete Browser-Tabs auf deinem Computer zugreifen. Du kannst Dateien bereitstellen, indem du sie hochlädst, einem unterstützten Projekt hinzufügst oder eine autorisierte verbundene App verwendest. Die Desktop-Version regelt den Zugriff auf lokale Dateien und Anwendungen über eigene Berechtigungen.

Wenn die
[Bibliothek](https://help.openai.com/en/articles/20001052-file-storage-and-library-in-chatgpt)
verfügbar ist, können geeignete hochgeladene oder erstellte Dateien dort gespeichert werden.
Die Administration kann festlegen, ob ChatGPT automatisch auf gespeicherte
Dateien in der Bibliothek zurückgreift. Auch wenn diese automatische Nutzung deaktiviert ist,
können Nutzende weiterhin gezielt auf Dateien zugreifen oder sie anhängen, sofern sie zu deren Nutzung berechtigt sind.

Siehe [Sandboxing für Code und Shell](/de-DE/codex/sandboxing?surface=web),
[Dokumente, Tabellen und Präsentationen erstellen und bearbeiten](https://help.openai.com/en/articles/20001278-creating-and-editing-documents-spreadsheets-and-presentations-with-chatgpt-work)
sowie
[Dateispeicherung und Bibliothek in ChatGPT](https://help.openai.com/en/articles/20001052-library-for-chatgpt).

## Netzwerkzugriff und externe Zieladressen

Work nutzt Tools wie die Ausführung von Code und Shell-Befehlen sowie den Cloud-Browser, um Aufgaben zu erledigen. Für jedes dieser Tools lassen sich die Berechtigungen konfigurieren.

- **Code und Shell-Befehle**: Der Zugriff auf das öffentliche Internet richtet sich nach der geltenden
  Workspace-Richtlinie und der individuellen Netzwerkeinstellung für Work. Ist der Zugriff auf das öffentliche
  Internet nicht erlaubt, können Befehle weiterhin von OpenAI genehmigte Zieladressen
  erreichen, die für die Funktion von Work erforderlich sind. Dadurch wird gesteuert, welche Netzwerkziele
  erreichbar sind, nicht, welche Befehle ausgeführt werden können.
- **Websuche**: Für die Suche gelten eigene Kontrollen, unabhängig von der Netzwerkeinstellung
  für Code und Shell in Work.

Sofern verfügbar, findest du die individuelle Einstellung für Code und Shell unter
**Einstellungen** \> **Datenkontrollen** \> **Netzwerkzugriff für Work**. Das Aktivieren von **Öffentlichen
Internetzugang erlauben** setzt geltende administrative
Einschränkungen nicht außer Kraft. Wenn du die Option deaktivierst, werden Code und Shell-Befehle auf die erforderlichen
Zieladressen der verwalteten Zulassungsliste beschränkt. Verbundene Apps, die
Websuche und der Cloud-Browser werden dadurch nicht deaktiviert.

Änderungen an der Netzwerkeinstellung für Code und Shell werden wirksam, nachdem der aktuelle Durchlauf
abgeschlossen ist und Work seine Ausführungsumgebung aktualisiert hat. Siehe
[Sandboxing für Code und Shell](/de-DE/codex/sandboxing?surface=web) und
[Zugriffskontrollen für Work](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

Kontrollen für ausgehende Interaktionen sind unabhängig von
[IP-Zugriffsbeschränkungen für den Workspace](https://help.openai.com/en/articles/12111596-ip-allowlisting-for-chatgpt),
die den eingehenden Zugriff auf den ChatGPT-Workspace oder die Compliance API begrenzen.

## Cloud-Browser und Website-Zugriff

Der
[Cloud-Browser](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)
ist eines der Tools, die ChatGPT Work verwenden kann, und unterscheidet sich vom
[In-App-Browser](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app).
Er wird auf einem entfernten System ausgeführt und nutzt eine Browsersitzung, die vom lokalen
Browser der jeweiligen Person getrennt ist. Er kann nicht auf lokale Tabs, Erweiterungen,
den Browserverlauf, gespeicherte Passwörter oder authentifizierte lokale Sitzungen zugreifen.

Der Cloud-Browser kann durch öffentliche Websites navigieren, Informationen in unterstützte öffentliche Formulare eingeben und relevante Informationen aus einer genehmigten App für eine Aufgabe auf einer Website nutzen. In Enterprise- und Edu-Workspaces ist die Anmeldung auf Websites über den Cloud-Browser nicht verfügbar. Die Verfügbarkeit des Browsers hängt von deinem Tarif, deiner Region, dem Stand der Einführung und den Workspace-Berechtigungen ab. Bei Enterprise-Workspaces muss die Administration zusätzlich zum Zugriff auf Work auch den Zugriff auf den Cloud-Browser aktivieren.

Für Website-Zugriffe und Aktionen gelten separate Kontrollen:

- Vor dem Besuch einer neuen Website fragt ChatGPT standardmäßig nach. Sofern verfügbar,
  können Nutzende zwischen **Immer nachfragen**, **Automatisch genehmigen** und **Immer zulassen** wählen sowie einzelne Websites zulassen oder
  blockieren. Bei **Automatisch genehmigen** werden Risiken automatisch geprüft.
**Immer zulassen** deaktiviert die interaktive Überprüfung des Website-Zugriffs. Die Administration
  kann die Genehmigungseinstellungen für Nutzende ebenfalls einschränken und
  beispielsweise **Immer zulassen** für den gesamten Workspace deaktivieren.
- Die Freigabe einer Website genehmigt nicht automatisch jede Aktion auf dieser Website. ChatGPT kann vor Aktionen, die finanzielle, rechtliche, kontobezogene oder andere folgenreiche Verpflichtungen nach sich ziehen könnten, eine gesonderte Bestätigung anfordern.

Nutzende können verfügbare Screenshots von Webseiten und die Wiedergabe der Browseraktivität in einem Work-Chat einsehen. Diese für Nutzende sichtbaren Aufzeichnungen belegen weder, dass ein Export über die Compliance API möglich ist, noch, dass der Administration ein vollständiger Ausführungsverlauf zur Verfügung steht.

Siehe
[Den Cloud-Browser in ChatGPT verwenden](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)
und [Browser](/de-DE/codex/browser?surface=web).

## Verbundene Anwendungen, Anmeldedaten und Berechtigungen

Eine verbundene App oder ein Plug-in gewährt Work nur über die von deinem Workspace zugelassene Integration und im Rahmen der für diese Verbindung erteilten Berechtigungen Zugriff. Die Administration kann im Admin-Dashboard die Verfügbarkeit von Plug-ins und Apps, den Zugriff nach Workspace-Rollen, externe Autorisierungen, Aktionseinstellungen und Berechtigungen im Quellsystem steuern.

In Enterprise- und Edu-Workspaces sind Plug-ins und die zugrunde liegenden Apps standardmäßig deaktiviert. In Business-Workspaces sind Plug-ins und Apps standardmäßig aktiviert. Wenn ein Plug-in verfügbar gemacht wird, wird dadurch weder die erforderliche App automatisch aktiviert noch Zugriff auf ein Konto gewährt. Die erforderliche Verbindung muss für ein persönliches, gemeinsam genutztes oder einem Agenten gehörendes Konto autorisiert sein, bevor ChatGPT Work darauf zugreifen kann. Eine gemeinsam genutzte oder einem Agenten gehörende Verbindung nutzt die Berechtigungen des verbundenen Kontos im Quellsystem. Diese können von den Berechtigungen der anfragenden Person abweichen.

Sofern unterstützt, kann die Administration eine App auf Aktionen ohne Schreibzugriff oder auf eine genehmigte Auswahl an Aktionen beschränken. Über die Berechtigungseinstellungen einer App lässt sich außerdem festlegen, ob ChatGPT vor der Nutzung einer App, vor Änderungen oder vor wichtigen Aktionen nachfragt. Nicht jede App unterstützt dieselben Kontrollmöglichkeiten für Aktionen, und nicht jede Aktion erfordert eine gesonderte Bestätigung durch einen Menschen.

Bei synchronisierten Apps kann es dauern, bis Änderungen an den Quellinhalten oder Berechtigungen sichtbar werden. Wenn die Verbindung zu einer App getrennt wird, werden Informationen, die bereits in einem Chat, einer erstellten Datei oder einem Datensatz mit eigener Aufbewahrungsrichtlinie gespeichert sind, nicht automatisch entfernt.

Siehe
[Administrative Kontrollen, Sicherheit und Compliance für Plug-ins und Apps](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business),
[Kontrollen für Plug-ins](/de-DE/codex/enterprise/apps-and-connectors),
[Von der Administration verwaltetes Setup für Google Workspace](https://help.openai.com/en/articles/10929079-google-workspace-admin-managed-setup)
und [ChatGPT-Apps mit Synchronisierung](https://help.openai.com/en/articles/10847137-chatgpt-apps-with-sync).

## Datenschutz und Umgang mit Daten

ChatGPT Work befolgt die für deinen ChatGPT-Workspace geltenden Richtlinien zu Datenschutz, Sicherheit und dem Umgang mit Daten. Für Chats, hochgeladene Dateien, erstellte Dateien, verbundene Anwendungen und Browserdaten können unterschiedliche Aufbewahrungs- und Löschregeln gelten.

Weitere Informationen findest du unter [Datenschutz für Unternehmen](https://openai.com/enterprise-privacy/),
[Aufbewahrungsrichtlinien für Chats und Dateien](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt),
[Datenresidenz und Inferenzresidenz](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)
sowie in den [FAQ zur Administration von ChatGPT Work](/de-DE/codex/enterprise/work-admin-faq).

### Die Aufbewahrung richtet sich nach dem Datentyp

- **Work-Chats:** Es gelten die Einstellungen des jeweiligen ChatGPT-Workspace zur
  Aufbewahrung und Löschung von Chats.
- **In der Bibliothek gespeicherte Dateien:** Es gelten die Aufbewahrungsregeln für Dateien und
  den jeweiligen Workspace. Wenn ein Chat gelöscht wird, bleiben Dateien in der
  Bibliothek erhalten.
- **Projektdateien:** Sie bleiben im Projekt, bis das Projekt gelöscht wird.
  Dabei gelten die entsprechenden Löschregeln und Ausnahmen.
- **Temporäre Uploads außerhalb der Bibliothek:** Bei Enterprise können temporäre Uploads
  nach 48 Stunden ablaufen, sofern keine abweichende Aufbewahrungseinstellung gilt.
- **Gespeicherte Erinnerungen, sofern aktiviert:** Für sie gelten gesonderte Einstellungen für Erinnerungen.
- **Cookies des Cloud-Browsers:** Sie bleiben von lokalen Browserdaten getrennt.
  Nutzende können sie in den Einstellungen des Cloud-Browsers löschen.
- **Datensätze der Plattform für Compliance-Protokolle:** Sie bleiben 30 Tage lang auf der Plattform verfügbar.
  Für exportierte Kopien gilt die Aufbewahrungsrichtlinie des empfangenden Systems.
- **Daten verbundener Anwendungen:** Für Quelldatensätze gelten die Richtlinien der verbundenen
  Anwendung. Für Kopien, die in einem Chat, einer Datei oder einem synchronisierten
  Index gespeichert sind, gelten zusätzlich die entsprechenden Speicher- und Aufbewahrungsregeln von OpenAI.

Das Löschen eines Chats, das Beenden einer Work-Aufgabe, das Löschen von Browser-Cookies und das Aufbewahren von Compliance-Datensätzen sind unterschiedliche Vorgänge. Wenn ein Chat gelöscht wird, verschwindet er aus der Ansicht und wird zur dauerhaften Löschung innerhalb von 30 Tagen vorgemerkt, vorbehaltlich der veröffentlichten Ausnahmen in Bezug auf Sicherheit, rechtliche Vorgaben und Deidentifizierung.

Siehe
[Aufbewahrungsrichtlinien für Chats und Dateien](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt),
[Erinnerung in ChatGPT](https://help.openai.com/en/articles/8590148-memory-in-chatgpt-faq)
sowie die
[OpenAI-Compliance-Plattform](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).

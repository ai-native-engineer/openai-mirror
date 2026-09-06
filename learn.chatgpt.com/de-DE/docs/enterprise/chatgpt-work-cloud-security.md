<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/chatgpt-work-cloud-security -->

ChatGPT Work ist Teil deines bestehenden ChatGPT-Workspaces und unterliegt dessen geltenden Richtlinien zu Datenschutz, Sicherheit und Umgang mit Daten. Zu den bestehenden Schutzmaßnahmen für Business-, Enterprise- und Edu-Workspaces gehört die Verschlüsselung bei der Übertragung und im Ruhezustand. OpenAI verwendet Geschäftsdaten standardmäßig nicht zum Trainieren seiner Modelle.

Work Cloud bietet außerdem eine gehostete Aufgabenausführung sowie optionale Tools, die auf verbundene Systeme zugreifen oder autorisierte Aktionen ausführen können. Prüfe die Berechtigungen, Aufbewahrungseinstellungen und verfügbaren Auditprotokolle für die Funktionen, die deine Organisation aktiviert.

Funktionen und Kontrollmöglichkeiten hängen vom Workspace-Tarif, dem Rollout, der Konfiguration
und der verbundenen Integration ab. Mehr zum übergreifenden Ausführungsmodell findest du in der
[Übersicht zu ChatGPT Work](/de-DE/codex/enterprise/chatgpt-work-overview).

## Sicherheit auf einen Blick

- Aufgaben in der Cloud laufen auf einer von OpenAI verwalteten Infrastruktur, nicht auf dem Gerät der nutzenden Person.
- Eine Cloud-Aufgabe übernimmt von diesem Gerät weder lokale Dateien noch Desktop-Anwendungen, Browsersitzungen oder Zugriff auf private Netzwerke.
- Verbundene Apps nutzen die Berechtigungen des autorisierten Kontos. Das kann ein persönliches Konto, ein gemeinsam genutztes Konto oder das Konto eines Agenten sein.
- Einstellungen auf Workspace-Ebene und für einzelne Funktionen regeln den Zugriff auf Work, die lokale Ausführung, das Browsen in der Cloud, verbundene Apps und den Netzwerkzugriff bei der Ausführung von Code oder Shell-Befehlen.
- Daten aus Business-, Enterprise- und Edu-Workspaces werden bei der Übertragung und im Ruhezustand verschlüsselt und standardmäßig nicht zum Trainieren von OpenAI-Modellen verwendet.
- Aufbewahrung und Verfügbarkeit von Auditdaten hängen von der Datenkategorie, dem Speicherort, dem Ereignis und der jeweiligen Produktkonfiguration ab.

## Wo Cloud-Aufgaben ausgeführt werden

Cloud-Aufgaben lassen sich in den unterstützten Web-, Mobil- oder Desktop-Versionen von ChatGPT starten. Work läuft im Web und auf Mobilgeräten in der Cloud. Die Desktop-App kann Cloud-Aufgaben oder lokale Aufgaben ausführen, wenn die entsprechenden Berechtigungen verfügbar und aktiviert sind.

Das Gerät der nutzenden Person liegt innerhalb des von der IT der Organisation verwalteten Vertrauensbereichs und außerhalb der von OpenAI betriebenen Systeme. Wird eine Cloud-Aufgabe über die Desktop-App gestartet, erhält sie dadurch keinen direkten Zugriff auf den Computer dieser Person. Die Ausführung bleibt in der von OpenAI verwalteten Umgebung, unabhängig davon, über welche Oberfläche sie gestartet wurde.

Work Cloud nutzt den Harness von Codex zur Aufgabenausführung. Work und Codex teilen grundlegende Mechanismen zur Ausführung und Isolation, bieten aber nicht dieselben Tools, Berechtigungen und administrativen Kontrollmöglichkeiten. Die Kundenorganisation kontrolliert den Zugriff auf den Workspace, genehmigte Verbindungen und die Informationen, die einer Aufgabe bewusst bereitgestellt werden. OpenAI verwaltet die gehostete Ausführungsumgebung.

Work Cloud läuft auf einer gemeinsam genutzten, von OpenAI verwalteten Infrastruktur. Im derzeit unterstützten Ausführungspfad laufen Aufgaben in VM-gestützten Sandboxen. Ihr Ausführungszustand ist der authentifizierten Person zugeordnet, die das Konto im Workspace nutzt. Work kann eine Umgebung für mehrere Aufgaben wiederverwenden oder sie ersetzen und dabei Zustandsdaten beibehalten, sofern diese dafür infrage kommen. Das bedeutet nicht, dass jede Aufgabe einen neuen Container erhält oder jeder Kundenorganisation ein eigener physischer Host zur Verfügung steht. Die Container von Work Cloud werden nicht kundenseitig bereitgestellt, gehostet oder verwaltet.

## Worauf eine Cloud-Aufgabe zugreifen kann

Eine Cloud-Aufgabe kann Informationen nutzen, die über einen autorisierten Zugriffsweg bereitgestellt werden:

- Informationen, die eine Person in eine Unterhaltung eingibt.
- Dateien, die bewusst hochgeladen, aus der Bibliothek angehängt oder über ein Projekt bereitgestellt werden.
- Inhalte, die über eine aktivierte App und eine autorisierte Kontoverbindung abgerufen werden.
- Website-Inhalte, auf die über einen aktivierten Cloud-Browser oder eine andere erlaubte Webfunktion zugegriffen wird, unter Beachtung der geltenden Zugriffskontrollen.

Eine Cloud-Aufgabe übernimmt nicht direkt den Zugriff auf lokale Dateien, installierte Anwendungen oder die Browsersitzung der nutzenden Person. Wenn ein Gerät Zugriff auf ein Unternehmens-VPN, eine interne Website oder ein privates Netzwerk hat, erhält die Cloud-Aufgabe dadurch keinen entsprechenden Zugriff.

Eine autorisierte Verbindung kann Informationen aus einem internen System über ihren eigenen Zugriffsweg bereitstellen. Dadurch erhält die Cloud-Aufgabe keinen uneingeschränkten Zugriff auf Geräte oder Netzwerke von Mitarbeitenden.

## Apps, Plug-ins und verbundene Konten

Eine App kann Work Zugriff auf Informationen oder Aktionen in einem anderen System geben. Ein Plug-in kann eine App als eines seiner zugrunde liegenden Tools nutzen. Die Bereitstellung eines Plug-ins führt nicht automatisch dazu, dass die zugrunde liegende App aktiviert, ein Konto autorisiert oder jede mögliche Aktion der Integration genehmigt wird.

Eine Aufgabe, die eine verbundene App direkt oder über ein Plug-in nutzt, kann nur ausgeführt werden, wenn folgende Bedingungen erfüllt sind:

- Die App und alle Plug-ins, die sie benötigen, sind im Workspace aktiviert.
- Die Person verfügt über die erforderlichen Zugriffsrechte im Workspace oder über ihre Rolle.
- Die Verbindung nutzt ein autorisiertes Konto: ein persönliches Konto, ein gemeinsam genutztes Konto oder das Konto eines Agenten.
- Das verbundene Konto, die genehmigten Scopes und die verfügbaren Einstellungen für App-Aktionen erlauben den Zugriff auf die angeforderten Informationen oder die gewünschte Operation.

Bei Apps, die die **Aktionssteuerung** unterstützen, können Admins Aktionen ohne Schreibzugriff,
alle Aktionen oder eine benutzerdefinierte Auswahl zulassen. Die **App-Berechtigungen** legen fest,
wann ChatGPT eine Bestätigung für die Nutzung einer App anfordert. Je nach App und
Workspace können die Optionen **Immer nachfragen**, **Alle Änderungen**, **Wichtige
Aktionen** und **Nie nachfragen** verfügbar sein. Bei der Option **Alle Änderungen** können unterstützte Lesezugriffe
ohne Rückfrage erfolgen, während Änderungen eine Bestätigung erfordern.

Ein autorisierter Schreibzugriff kann ohne Rückfrage erfolgen, wenn die konfigurierte Richtlinie dies erlaubt. Dadurch werden weder die zulässigen Aktionen der App noch der Workspace-Zugriff oder die Berechtigungen des verbundenen Kontos erweitert. ChatGPT kann bestimmte Aktionen mit hohem Risiko weiterhin blockieren.

Vergewissere dich, dass das Plug-in und jede zugrunde liegende App im Workspace verfügbar sind.
Prüfe die Entscheidungen zum rollenbasierten Zugriff, zur Autorisierung des verbundenen Kontos und zu den Aktionsberechtigungen
jeweils gesondert. Siehe
[Kontrollen für Plug-ins](/de-DE/codex/enterprise/apps-and-connectors).

### Persönliche und gemeinsam genutzte Verbindungen

Eine persönliche Verbindung nutzt im Quellsystem die Berechtigungen der Mitarbeitenden, deren Konto verbunden ist. Eine gemeinsam genutzte Verbindung oder die Verbindung eines Agenten nutzt stattdessen die Berechtigungen des jeweils verbundenen Kontos. Dieses Konto kann möglicherweise auf Informationen zugreifen oder Aktionen ausführen, die der anfragenden Person mit einem persönlichen Konto nicht zugänglich wären.

Bevor du eine gemeinsam genutzte Verbindung aktivierst, beschränke die Berechtigungen und
Scopes des Kontos, lege fest, wer es nutzen darf, und prüfe die Aktionen, die es ausführen kann. Siehe
[Verbindungen und Berechtigungen für Workspace-Agenten](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business).

Inhalte, die aus einer verbundenen App abgerufen werden, werden nicht automatisch als Datei in der Bibliothek gespeichert. Werden diese Inhalte später in einer Unterhaltung, einem Projekt, der Bibliothek oder einem synchronisierten Index gespeichert, gelten für diese Kopie die Regeln des jeweiligen Speicherorts.

## Cloud-Browser und Netzwerkzugriff

Der Cloud-Browser, die Websuche, verbundene Apps und der Netzwerkzugriff bei der Ausführung von Code oder Shell-Befehlen sind eigenständige Funktionen. Wird eine davon eingeschränkt, werden die anderen dadurch nicht automatisch deaktiviert.

### Cloud-Browser

Der Cloud-Browser ist ein gehostetes Tool, mit dem eine Work-Aufgabe mit Websites interagieren kann. Wenn du ChatGPT in einem Webbrowser oder einer Desktop-App öffnest, wird dadurch das Browsen in der Cloud nicht aktiviert. Eine Cloud-Aufgabe kann auch ohne diese Funktion ausgeführt werden.

Der gehostete Browser übernimmt weder das lokale Browserprofil noch offene Tabs, bestehende Anmeldungen, gespeicherte Passwörter, den Passwortmanager oder den Browserverlauf der nutzenden Person. Wo dies unterstützt wird, können sich Nutzende über einen sicheren gehosteten Anmeldeprozess separat anmelden. Dadurch erhält der gehostete Browser keinen Zugriff auf ihre lokale Browsersitzung.

Unterstützte Interaktionen mit Websites können öffentliche Formulare umfassen. Dabei lassen sich
Informationen aus einer autorisierten App mit einer Aufgabe auf einer Website kombinieren. Sofern verfügbar,
umfassen die Website-Berechtigungen **Immer nachfragen**, **Automatisch genehmigen** und **Immer
erlauben**. Bei der Option **Automatisch genehmigen** erfolgen automatisierte Risikoprüfungen. **Immer erlauben**
hebt die interaktive Überprüfung des Website-Zugriffs auf. Keine der beiden Optionen erteilt
neue App-Berechtigungen oder genehmigt sämtliche Aktionen auf einer Website. Folgenreiche Aktionen können
weiterhin eine gesonderte Bestätigung erfordern.

Damit eine Work-Aufgabe den Cloud-Browser in einem Enterprise-Workspace nutzen kann,
müssen Admins sowohl den Zugriff auf Work als auch auf den Cloud-Browser aktivieren. Siehe
[Den Cloud-Browser in ChatGPT nutzen](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt).

### Netzwerkzugriff für Code und Shell-Befehle

Der Zugriff auf das öffentliche Internet bei der Ausführung von Code oder Shell-Befehlen unterliegt einer eigenen Netzwerkrichtlinie. Ist der öffentliche Internetzugang deaktiviert, können die für ChatGPT Work erforderlichen Netzwerkziele über eine verwaltete Liste zulässiger Ziele weiterhin erreichbar bleiben.

Die Liste zulässiger Ziele gilt für Netzwerkziele, nicht für Shell-Befehle. Wird der öffentliche Internetzugang für die Ausführung von Code oder Shell-Befehlen deaktiviert, werden dadurch allein weder der Cloud-Browser noch die Websuche oder verbundene Apps deaktiviert. Änderungen an der Netzwerkeinstellung werden wirksam, nachdem die aktuelle Code-Ausführung oder der aktuelle Shell-Befehl abgeschlossen ist und die Ausführungsumgebung aktualisiert wurde.

Siehe [Sandboxing für Code und Shell-Befehle](/de-DE/codex/sandboxing?surface=web).

## Umgang mit Daten und Aufbewahrung

Für Work Cloud gelten die oben beschriebenen Datenschutz- und Sicherheitsmaßnahmen
des jeweiligen ChatGPT-Workspaces. Siehe
[Datenschutz für Unternehmen](https://openai.com/enterprise-privacy/).

Für Informationen, die mit einer Cloud-Aufgabe verbunden sind, gelten keine einheitlichen Aufbewahrungsfristen:

| Datenkategorie                        | Aufbewahrung und Löschung                                                                                                                                                                                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Work-Unterhaltungen                   | Unterliegen den Workspace-Einstellungen zur Aufbewahrung von Unterhaltungen. Für gelöschte Chats ist in der Regel die endgültige Löschung innerhalb von 30 Tagen vorgesehen. Dabei gelten die veröffentlichten Ausnahmen aus Sicherheits- und Rechtsgründen sowie im Zusammenhang mit der De-Identifizierung.                                                                                |
| Gehosteter Ausführungszustand und Snapshots | Für sie gilt ein anderer Lebenszyklus als für Unterhaltungen und Dateien. Der Zugriff auf den Ausführungszustand ist auf die Person beschränkt, die das Konto nutzt. Bei gespeicherten Snapshots, die dafür infrage kommen, wird die Workspace-Einstellung zur Aufbewahrung von Unterhaltungen berücksichtigt. Wird eine Aufgabe beendet oder ein Chat gelöscht, werden nicht sofort sämtliche zugehörigen Artefakte gelöscht. |
| In der Bibliothek gespeicherte Dateien               | Hochgeladene oder generierte Dateien unterliegen den geltenden Aufbewahrungsregeln für die Bibliothek und den Workspace. Das Löschen einer Unterhaltung löscht keine Datei, die in der Bibliothek gespeichert ist.                                                                                                                                      |
| Projektdateien                        | Bleiben ihrem Projekt zugeordnet, bis sie entfernt werden oder das Projekt gelöscht wird. Dabei gelten die jeweiligen Löschregeln.                                                                                                                                                                       |
| Gespeicherte Erinnerungen, sofern aktiviert         | Es gelten separate Einstellungen für Erinnerungen. Das Löschen einer Unterhaltung entfernt nicht zwangsläufig eine bereits gespeicherte Erinnerung.                                                                                                                                                                             |
| Temporäre Uploads                    | Temporäre Enterprise-Uploads außerhalb der Bibliothek können nach 48 Stunden ablaufen, sofern sie dafür infrage kommen und keine andere Aufbewahrungseinstellung gilt.                                                                                                                                                      |
| Inhalte verbundener Apps                | Datensätze im Quellsystem unterliegen dessen Richtlinien. Für Kopien, die in einer Unterhaltung, einem Projekt, der Bibliothek oder einem synchronisierten Index gespeichert werden, gelten die Regeln des jeweiligen Speicherorts.                                                                                                                         |
| Daten des Cloud-Browsers                   | Die Daten des gehosteten Browsers sind von lokalen Browserdaten getrennt. Gespeicherte Cookies des Cloud-Browsers kannst du über die entsprechenden Einstellungen entfernen.                                                                                                                                                    |
| Compliance-Datensätze                   | Datensätze der Plattform für Compliance-Protokolle sind 30 Tage lang verfügbar. Exportierte Kopien unterliegen der Aufbewahrungsrichtlinie des empfangenden Systems.                                                                                                                                                               |

Eine Unterhaltung zu löschen, eine Datei aus der Bibliothek oder eine gespeicherte Erinnerung zu entfernen,
die Verbindung zu einer App zu trennen und die Daten des gehosteten Browsers zu löschen, sind separate Aktionen.
Prüfe den jeweiligen Speicherort, statt davon auszugehen, dass eine Aktion
alle Kopien entfernt. Siehe
[Aufbewahrungsrichtlinien für Chats und Dateien](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt).

Wenn relevanter Kontext aus Unterhaltungen und der Aufgabenausführung erhalten bleibt, kann das Work helfen,
unterbrochene Aufgaben fortzusetzen, auf frühere Schritte zurückzugreifen und konsistentere Ergebnisse zu liefern.
Kürzere Aufbewahrungsfristen oder das Löschen von Daten können diese Kontinuität beeinträchtigen. Wähle daher Einstellungen,
die Sicherheitsanforderungen und den Nutzen des Ablaufs in Einklang bringen.

Enterprise- und Edu-Workspaces, die die entsprechenden Voraussetzungen erfüllen, können Enterprise Key Management
für unterstützte gespeicherte Inhalte nutzen. Dazu zählen unterstützte Snapshots der gehosteten Ausführungsumgebung,
wenn eine kundenseitig verwaltete Verschlüsselung erforderlich ist. Welche Daten abgedeckt sind, hängt von der Datenkategorie
und der Bereitstellung ab. Die Rotation eines Schlüssels löscht keine vorhandenen Daten und sperrt für sich genommen
auch nicht den Zugriff auf zuvor verschlüsselte Inhalte. Der Widerruf oder die Deaktivierung des Schlüsselzugriffs
ist eine separate Aktion, die unterstützte Arbeitsabläufe beeinträchtigen kann. Keine dieser Aktionen ersetzt
eine Aufbewahrungs- oder Löschrichtlinie.

Datenresidenz und Inferenzresidenz gelten nur für Inhalte, die die Voraussetzungen erfüllen, und
unterstützte Workloads. Maßgeblich sind die Vereinbarung der Organisation, die Region und
die Konfiguration. Für verbundene Apps, externe Anbieter sowie manche Verarbeitungsvorgänge oder
synchronisierte Indizes können separate Standortregeln gelten. Prüfe die Unterstützung für
das Produkt, die Integration und die Region. Siehe
[Datenresidenz und Inferenzresidenz](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt).

Die Einstellung [Keine Datenaufbewahrung](/api/docs/guides/your-data#zero-data-retention) der OpenAI API
gilt ausschließlich für die API und legt die Datenaufbewahrung für ChatGPT Work nicht fest.

## Administrative Zugriffskontrollen

Prüfe die Einstellungen, die für die einzelnen Teile einer Cloud-Aufgabe gelten:

- **Work Cloud und Work Lokal:** Wenn unabhängige Einstellungen verfügbar sind,
  verwalte Work in der Cloud und lokales Work getrennt unter **Workspace-Einstellungen** \>
**Berechtigungen & Rollen**. In anderen Workspaces kann lokales Work über dieselbe Einstellung
  wie Codex Lokal gesteuert werden.
- **Apps und Plug-ins:** Lege fest, welche Integrationen verfügbar sind und welche
  Personen oder Rollen sie nutzen können.
- **Aktionen verbundener Konten:** Prüfe die Kontoberechtigungen, die Berechtigungsbereiche der Anwendungen
  sowie die verfügbaren Einstellungen für Aktionen oder Bestätigungen.
- **Browser und Netzwerkzugriff:** Bewerte den Zugriff auf den Cloud-Browser und den Zugriff
  auf öffentliche Netzwerke bei der Code- oder Shell-Ausführung unabhängig voneinander.

Aktiviere **Work Cloud** nur für Personen oder Gruppen, die dafür freigegeben sind. Wenn getrennte Einstellungen für
**Work Cloud** und **Work Lokal** verfügbar sind, aktiviere **Work Cloud**
und deaktiviere **Work Lokal** für die vorgesehene Rolle, um Work in der Cloud ohne
lokale Ausführung zu erlauben. Wenn lokales Work und Codex über dieselbe Einstellung gesteuert werden, prüfe die Auswirkungen
auf beide, bevor du die lokale Ausführung deaktivierst. Diese Einstellungen verhindern nicht, dass eine
autorisierte Person bewusst eine Datei in eine Cloud-Aufgabe hochlädt.

Bei unterstützten Rollenberechtigungen mit den Zuständen **Standard**, **Ein** und **Aus** gilt:
**Standard** übernimmt die Workspace-Einstellung, **Ein** gewährt Zugriff und **Aus**
entzieht den Zugriff über diese Rolle. Hat eine Person mehrere benutzerdefinierte Rollen, kann eine andere
Rolle weiterhin Zugriff gewähren. Einige Einstellungen für Work und Plug-ins haben dagegen
nur zwei mögliche Zustände. Prüfe den tatsächlichen Zugriff über alle zugewiesenen Rollen hinweg. Siehe
[Rollenbasierte Zugriffskontrolle](https://help.openai.com/en/articles/11750701-rbac).

Sofern verfügbar, gilt die Berechtigung **Work Cloud** für die unterstützten Oberflächen im Web,
auf Mobilgeräten und auf dem Desktop. Sie legt nicht gesondert fest, über welche dieser
Oberflächen Cloud-Aufgaben ausgeführt werden können. Ziehe die Geräteverwaltung oder andere
Zugriffskontrollen in Betracht, wenn bei einer Bereitstellung eine bestimmte Oberfläche ausgeschlossen werden muss.

## Einblick in Audit- und Compliance-Daten

Für Enterprise- und Edu-Workspaces, die die entsprechenden Voraussetzungen erfüllen, kann die Plattform für Compliance-Protokolle
unterstützte Prompts und Antworten aus Work enthalten. Aufrufe verbundener Apps werden separat
protokolliert. Welche Audit-Datensätze im Quellsystem verfügbar sind, hängt von der Integration ab.
Unterstützte Compliance-Endpunkte können Zugriff auf Dateien in der Bibliothek ermöglichen, die dafür infrage kommen.

Der Umfang der Protokollierung hängt vom Ereignis und dem System ab, in dem es auftritt. Gehe nicht davon aus,
dass jeder Shell-Befehl, jede Browserinteraktion, jeder App-Aufruf, jede Dateioperation oder
jede Genehmigung in einem kundenseitig einsehbaren Compliance-Export erscheint.

Über die Endpunktüberwachung kannst du den ChatGPT-Client oder den Netzwerkverkehr auf verwalteten
Geräten beobachten, aber keine Aktionen innerhalb der gehosteten Ausführungsumgebung einsehen. Nutze
stattdessen die unterstützten Aufzeichnungen zu Work, zur Compliance und aus verbundenen Systemen.

Prüfe, welche Compliance-Ereignisse aktuell erfasst werden, und berücksichtige dabei die Workspace-Berichte,
die Audit-Protokolle verbundener Systeme sowie die Aufbewahrungsrichtlinien der Systeme, die
exportierte Datensätze erhalten. Siehe die
[OpenAI-Compliance-Plattform](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).

## Starte mit einem kleinen Pilotprojekt

Wähle eine praktische Aufgabe für eine kleine Gruppe aus. Ein Sicherheitsteam könnte beispielsweise
einen freigegebenen Sicherheitshinweis eines Anbieters mit einem zur Nutzung freigegebenen Inventar abgleichen und den
Entwurf einer Bewertung der Betroffenheit prüfen, bevor es über weitere Schritte entscheidet. Wenn der Cloud-Browser oder
verbundene Apps nicht verfügbar sind, stelle den Hinweis und einen freigegebenen Inventarauszug
direkt bereit.

Erlaube nur die für die Aufgabe erforderlichen Zugriffe. Prüfe die Berechtigungen verbundener Konten,
die Aufbewahrungseinstellungen und die verfügbaren Audit-Datensätze. Kläre außerdem, an welcher Stelle eine Person
das Ergebnis überprüfen sollte, bevor du den Zugriff ausweitest. Hinweise zur Rollout-Planung findest du im
[Leitfaden für den administrativen Rollout](/de-DE/codex/enterprise/admin-setup).

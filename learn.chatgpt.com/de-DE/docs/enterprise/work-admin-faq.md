<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/work-admin-faq -->

ChatGPT Work bringt die Technologie hinter Codex für längere,
mehrstufige Aufgaben in ChatGPT. Es kann Kontext aus Chats, Dateien,
Workspace-Ressourcen und verbundenen Systemen zusammentragen, genehmigte Tools verwenden
und Ergebnisse zur Überprüfung bereitstellen. Zugriff, Kontext, Aktionen, Netzwerkverhalten und Credit-Verbrauch hängen von
Tarif, Workspace-Einstellungen, Berechtigungen der Quellsysteme und Oberfläche ab.

## Übersicht

Mit ChatGPT Work können Nutzende längere, mehrstufige Aufgaben an ChatGPT delegieren. Es kann
Informationen aus verbundenen Quellen zusammentragen, schrittübergreifend Zusammenhänge durchdenken, Dokumente,
Präsentationen oder Analysen erstellen und die Ergebnisse zur Überprüfung vorlegen.

ChatGPT Work ist auf unterstützten Web-, Mobil- und Desktop-Oberflächen für
Tarife und Workspaces verfügbar, die die Voraussetzungen erfüllen. Wo dies unterstützt wird, können Personen mit Inhaberrolle oder autorisierte
Admins Work Cloud, Work Local und Codex Local über jeweils eigene
Berechtigungen verwalten. In berechtigten Enterprise- und Edu-Workspaces umfasst die Standardrolle im Workspace
Work, sofern autorisierte Admins die Funktion nicht deaktivieren. Browser- und
Netzwerkkontrollen schränken Work Cloud zusätzlich ein. Die Verfügbarkeit hängt von Rolle,
Tarif, Workspace und Region ab. Weitere Informationen findest du unter
[ChatGPT Work und Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

Diese FAQ erläutern, wie Admins ChatGPT Work verwalten: Zugriffs- und Datenkontrollen,
Compliance und Transparenz, Nutzung und Ausgaben, Reaktion auf Vorfälle sowie
Vorgehensweisen beim Rollout. Informationen zum gehosteten Ausführungsmodell und zu Sicherheitsgrenzen findest du in der
[Übersicht zu ChatGPT Work](/de-DE/codex/enterprise/chatgpt-work-overview).

## Zentrale administrative Kontrollen

Admins steuern ChatGPT Work über folgende Kontrollebenen:

- **Zugriff auf den Unternehmens-Workspace:** Identitäts- und Zugriffskontrollen regeln
  die Authentifizierung und den Zugriff auf den Workspace. Je nach Tarif und
  Konfiguration können administrativ verwaltete Identitätsfunktionen SSO,
  Domain-Verifizierung, SCIM-Provisionierung, die Verwaltung von Benutzerkonten über ihren Lebenszyklus und
  die Synchronisierung von Identitätsgruppen umfassen. SCIM und synchronisierte Identitätsgruppen sind
  in ChatGPT Business nicht enthalten. Nutzende können MFA für ihr OpenAI-Konto aktivieren.
  ChatGPT unterstützt keine Durchsetzung von MFA für den gesamten Workspace. Organisationen, die
  dies benötigen, sollten SSO und MFA über ihren Identitätsanbieter erzwingen. Verwalte
  SSO und die zugehörigen Identitätseinstellungen in der
[Global Admin Console](https://help.openai.com/en/articles/12289294-admin-portal).
  Weitere Informationen findest du unter [Multi-Faktor-Authentifizierung](https://help.openai.com/en/articles/7967234-enabling-or-disabling-multi-factor-authentication-mfa).
- **Zugriff auf ChatGPT Work im Workspace:** Sofern verfügbar, regelt Work Cloud
  die Nutzung von gehostetem Work auf unterstützten Web-, Mobil- und Desktop-Oberflächen. Work Local
  regelt die lokale Nutzung von Work auf dem Desktop, während Codex Local den unterstützten lokalen
  Codex-Zugriff in Desktop-, CLI- und IDE-Clients steuert. Einstellungen für Cloud-Browser und Netzwerk
  schränken Work Cloud zusätzlich ein. Benutzerdefinierte rollenbasierte Zugriffskontrolle (RBAC)
  und verfügbare Berechtigungen hängen von Tarif und Workspace ab.
- **Gruppenmitgliedschaft:** Synchronisiere bei Tarifen mit SCIM-Unterstützung Gruppen über
  einen Identitätsanbieter. So wird der Zugriff aktualisiert, wenn Beschäftigte der Organisation beitreten,
  ihre Rolle wechseln oder ausscheiden. Weitere Informationen findest du unter
[Gruppen und Provisionierung](/de-DE/codex/enterprise/groups-and-provisioning).
- **Workspace- und Mitgliederrollen:** Zu den integrierten Enterprise-Rollen gehören Owner,
  Admin, Member und Analytics Viewer. Bei unterstützten Tarifen regeln benutzerdefinierte Rollen und
  RBAC für Mitglieder den Zugriff auf ChatGPT Work, Plug-ins und andere Funktionen.
  Wo unterschiedliche Lizenzplatztypen gelten, benötigen Mitglieder außerdem einen Lizenzplatz mit ChatGPT. Ein
  reiner Codex-Lizenzplatz gewährt keinen Zugriff auf Work. Weitere Informationen findest du unter
[Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions).
- **Plug-ins und Apps:** Die Plug-in-Richtlinie regelt die Verfügbarkeit und
  Installation von Plug-ins. Der Zugriff auf Apps, Aktionskontrollen und das Verhalten bei Genehmigungen werden
  separat konfiguriert. Wo Workspace-Agenten verfügbar sind, gelten für sie eigene
  Kontrollen. Weitere Informationen findest du unter [Kontrollen für Plug-ins](/de-DE/codex/enterprise/apps-and-connectors),
[Plug-ins](/de-DE/codex/plugins) und im
[Whitepaper zur App-Sicherheit](https://cdn.openai.com/business-guides-and-resources/app-security-whitepaper.pdf).
- **Berechtigungen der Quellsysteme:** Nutzende können nur auf Inhalte und Aktionen zugreifen,
  die das Konto oder die gemeinsam genutzte Verbindung in der nativen Anwendung zulässt. Weitere Informationen findest du unter
[Administrative Kontrollen, Sicherheit und Compliance in Apps](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business).
- **Genehmigungen und Aktionsbeschränkungen:** Bei Apps, die Aktionssteuerung unterstützen,
  können Admins alle Aktionen, Aktionen ohne Schreibzugriff oder eine individuelle Auswahl zulassen und festlegen,
  wie neu hinzugefügte Aktionen behandelt werden. App-Berechtigungen bestimmen unabhängig davon,
  wann ChatGPT vor der Nutzung einer App nachfragt.
- **Credits:** ChatGPT Work und Codex haben ein gemeinsames Preismodell und teilen sich Credits und Nutzungslimits.
  Berechtigte Enterprise- und Edu-Admins können monatliche Limits pro Person über einen
  Standardwert für den Workspace, Gruppenstandardwerte und individuelle Ausnahmen festlegen. Nutzende können
  eine Erhöhung beantragen, wenn der Workspace dies zulässt. Für Business gilt ein separates
  Modell für Credits und Ausgabenkontrollen. Weitere Informationen findest du unter
[ChatGPT-Nutzungslimits und Ausgabenkontrollen](/de-DE/codex/enterprise/usage-limits).
- **Analysen und Berichte:** Die Global Admin Console und Workspace-Analysen
  ermöglichen Auswertungen zur Verbreitung und zum Credit-Verbrauch. Nutze die Compliance API und die Codex-Berichtsoberflächen
  für die jeweils dokumentierten Ereignisse und Produkte. Prüfe die
  aktuellen Schemata, bevor du die Erfassung bestimmter Prompts, Dateien,
  Genehmigungen, Aktionen, Fehler oder Tool-Aufrufe zusicherst. Weitere Informationen findest du unter
[Governance](/de-DE/codex/enterprise/governance).

## Zugriff, Daten, Systeme und Aktionen von Nutzenden

### Wie werden der Zugriff auf Daten und Systeme sowie Aktionen von Nutzenden geschützt?

Für ChatGPT Work gelten die Identitäts-, Zugriffs- und Berechtigungskontrollen, die bereits
in deinem ChatGPT-Workspace eingerichtet sind. Admins nutzen die Identitätsverwaltung,
Workspace-Rollen und bei berechtigten Tarifen
[RBAC](https://help.openai.com/en/articles/11750701-rbac), um festzulegen, wer ChatGPT Work
nutzen darf.

Wo dies unterstützt wird, lässt sich der Zugriff über
[SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
und Gruppensynchronisierung mit deinem Identitätsanbieter abgleichen. So kannst du Zugriff und Berechtigungen zentral verwalten,
wenn Beschäftigte der Organisation beitreten, ihre Rolle wechseln oder ausscheiden.

Die zugrunde liegenden Quellsysteme setzen die Berechtigungen des für den Vorgang verwendeten Kontos oder der genehmigten
gemeinsam genutzten Verbindung durch. Eine individuelle Verbindung nutzt den Zugriff der betreffenden
Person auf das Quellsystem. Eine Verbindung, die einem Agenten gehört oder gemeinsam genutzt wird, kann
berechtigten Nutzenden des Agenten über das verbundene Konto Zugriff gewähren, auch auf Daten oder
Aktionen, auf die ihr eigenes Konto nicht zugreifen könnte. Beschränke die Berechtigungsbereiche der Verbindung,
die verfügbaren Aktionen und den Personenkreis, der den Agenten nutzen kann, auf den vorgesehenen geschäftlichen Bedarf. Weitere Informationen findest du unter
[Verbindungen und Berechtigungen für Workspace-Agenten](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business).

<a id="how-does-work-access-data-and-context"></a>
<a id="how-does-work-mode-access-data-and-context"></a>

### Wie greift ChatGPT Work auf Daten und Kontext zu?

ChatGPT Work kann den aktuellen Chat, hochgeladene Dateien, Workspace-Ressourcen und
verbundene Systeme über genehmigte Apps und gegebenenfalls Plug-ins nutzen.
Je nach aktivierten Funktionen und Berechtigungen können dazu Dokumente,
Repositorys, Tickets, Kanäle, E-Mails und Kalender gehören. Frühere Dateien können über
den aktuellen Chat, unterstützte Projekte, autorisierten Zugriff auf die Bibliothek oder aktivierte automatische
Verweise auf die Bibliothek verfügbar sein. Für gespeicherte Erinnerungen gelten eigene
Kontrollen auf Workspace- und persönlicher Ebene.

Für jede Kontextquelle gelten eigene Kontrollen: Nutzende stellen den Chat-Kontext bereit,
Admins verwalten Workspace-Ressourcen, und verbundene Systeme setzen Authentifizierung
und Berechtigungen durch. ChatGPT Work kann nur auf Informationen zugreifen, die für die jeweilige Person oder eine
genehmigte gemeinsam genutzte Verbindung freigegeben sind.

Für ChatGPT Work gelten die entsprechenden Schutzmaßnahmen des ChatGPT-Workspaces. Datenresidenz, Aufbewahrung,
Protokollierung und Funktionsverfügbarkeit hängen von Tarif, Region, Oberfläche und verbundenem
System ab. Prüfe daher, was für deine Konfiguration abgedeckt ist.

### Welche Aktionen mit weitreichenden Auswirkungen sind eingeschränkt oder müssen überprüft werden?

Das Risiko variiert je nach Aktion. Das Lesen oder Erstellen von Entwürfen hat meist geringere Auswirkungen als das Ändern
von Daten, das Teilen von Informationen oder Aktionen in externen Systemen. Kombiniere Rollen, eng begrenzte
Berechtigungen und Zugangsdaten sowie unterstützte Genehmigungen, damit Aktionen mit größeren Auswirkungen
auf vertrauenswürdige, geprüfte Anwendungsfälle beschränkt bleiben.

Zu den gängigen Aktionskategorien gehören:

- **Lesen:** Auf Informationen aus genehmigten Quellen zugreifen, sie durchsuchen oder zusammenfassen,
  ohne die zugrunde liegenden Daten zu verändern.
- **Entwürfe erstellen:** Dokumente, E-Mails, Berichte, Code oder andere Inhalte vorbereiten,
  damit eine Person sie vor der Verwendung überprüfen kann.
- **Schreiben:** Einträge in verbundenen Systemen erstellen, aktualisieren oder löschen, etwa
  in Dokumenten, Tickets, Repositorys oder Projektmanagement-Tools.
- **Teilen:** Informationen senden, veröffentlichen oder anderweitig weiteren
  Personen, Systemen oder externen Zielen zugänglich machen.
- **Planen:** Eine Aufgabe zu einem späteren Zeitpunkt oder regelmäßig nach Zeitplan starten,
  ohne dass Nutzende jeden Durchlauf selbst starten müssen.
- **Ausführen:** Code, Shell-Befehle, Browserautomatisierung oder andere
  toolgestützte Aufgaben ausführen, die direkt mit externen Umgebungen interagieren.

Setze bei Aktionen mit größeren Auswirkungen auf menschliche Überprüfung, eingeschränkte Zugangsdaten, eng gefasste
Berechtigungsbereiche und unterstützte Genehmigungen. Für Aktionen von Plug-ins gelten weiterhin die
Berechtigungen und Sicherheitskontrollen der jeweiligen Integration.

## Compliance

<a id="how-does-work-support-enterprise-privacy-and-data-commitments"></a>
<a id="how-does-work-mode-support-enterprise-privacy-and-data-commitments"></a>

### Wie unterstützt ChatGPT Work die Zusagen zu Datenschutz und zum Umgang mit Daten für Unternehmen?

Für ChatGPT Work gelten die Zusagen zu Datenschutz, Sicherheit und zum Umgang mit Daten für den jeweiligen
ChatGPT-Workspace, abhängig von Tarif, Konfiguration, Oberfläche, Funktion
und Region. Bei ChatGPT Enterprise umfasst dies
[standardmäßig kein Training mit Unternehmensdaten](https://help.openai.com/en/articles/8983130-what-if-i-want-to-keep-my-history-on-but-disable-model-training),
Verschlüsselung bei der Übertragung und im Ruhezustand, Zugriffskontrollen auf Workspace-Ebene und
unterstützte Audit-Protokollierung.

Ob Datenresidenz, Inferenzresidenz, HIPAA oder ein Business Associate Agreement abgedeckt sind,
hängt vom Einzelfall ab. Prüfe die aktuellen
[Hinweise zur Daten- und Inferenzresidenz](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)
sowie die jeweilige Kundenvereinbarung für die genutzten Funktionen und Regionen.

Verbundene Dienste haben eigene Anforderungen an Aufbewahrung, Protokollierung, Zugriff, Datenresidenz und
Compliance. Wenn ChatGPT Work Plug-ins, Repositorys oder Drittanbietersysteme
nutzt, prüfe sowohl die Kontrollen des ChatGPT-Workspaces als auch die Kontrollen des verbundenen
Systems.

Bei Codex-Aktivitäten können sich Kontrollen auf Unternehmensebene auch auf Entwicklungsumgebungen,
Repositorys, konfigurierte Tools und damit verbundene Aktivitäten erstrecken. Lies ergänzend zu den Workspace-Kontrollen den
[Leitfaden für den administrativen Rollout](/de-DE/codex/enterprise/admin-setup) und den Abschnitt
[Governance](/de-DE/codex/enterprise/governance).

### Welche Daten werden gespeichert, aufbewahrt oder gelöscht?

Die Aufbewahrung und Löschung von Daten in ChatGPT Work richten sich nach dem Tarif des ChatGPT-Workspaces,
den administrativen Einstellungen und den genutzten Funktionen. Die Aufbewahrung kann je nach
den Informationen variieren, auf die ChatGPT Work zugreift. Für Unterhaltungen sowie für Dateien in der Bibliothek, die die Voraussetzungen erfüllen,
gelten die jeweiligen Workspace-Einstellungen. Für Projektdateien, vorübergehend
hochgeladene Dateien, gespeicherte Erinnerungen, Compliance-Ereignisse, synchronisierte App-Daten und
Datensätze von Drittanbietern können gesonderte Regeln für Aufbewahrung und Löschung gelten. Weitere Informationen findest du unter
[Aufbewahrungsrichtlinien für Chats und Dateien](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt).

ChatGPT Work kann Chat-Inhalte, hochgeladene oder generierte Dateien, Artefakte
und Ausführungsmetadaten erzeugen. Codex-Chats können außerdem Metadaten zu Repositorys oder Umgebungen,
Befehlsausgaben, Diffs und Protokolle erzeugen. Prüfe in der aktuellen Produktdokumentation und in der Dokumentation zur
[Compliance API](/de-DE/codex/enterprise/compliance-api) die genauen Angaben zu
Datenklassen, Aufbewahrungsfristen und Löschverfahren.

Prüfe die Aufbewahrungsanforderungen sowohl im ChatGPT-Workspace als auch in verbundenen
Unternehmenssystemen, damit die Richtlinien deiner Organisation zu Daten-Governance, Compliance und
Aufbewahrung von Unterlagen für jedes System gelten.

## Beobachtbarkeit

### Welche Nutzungsdaten stehen Admins oder Personen mit Inhaberrolle zur Verfügung?

Admins und Personen mit Inhaberrolle können Produktanalysen und Compliance-Protokolle nutzen, um unterschiedliche
Einblicke zu gewinnen. Die Global Admin Console bietet unterstützte Ansichten zur Verbreitung von ChatGPT und
Codex sowie zum Credit-Verbrauch. Welche Aufschlüsselungen nach Person, Produkt, Agent und Modell verfügbar sind,
hängt von der Analyseoberfläche und dem Workspace ab. Für berechtigte
Workspaces stellt die Compliance API Datensätze zu den erfassten ChatGPT-Unterhaltungen bereit,
einschließlich unterstützter Work-Aktivitäten in der Cloud. Der Umfang hängt von Produkt,
Oberfläche, Berechtigungen, verfügbarem Endpunkt und dokumentiertem Ereignisschema ab. Weitere Informationen findest du unter
[Workspace-Analysen](/de-DE/codex/enterprise/workspace-analytics) und
[Compliance API](/de-DE/codex/enterprise/compliance-api).

### Werden Prompts, Ausgaben, Dateien, Aktionen oder Tool-Aufrufe protokolliert?

Für berechtigte Enterprise- und Edu-Workspaces stellt die Plattform für Compliance-Protokolle
Prompts von Work-Nutzenden und Antworten von Agenten bereit.
[Aufrufe verbundener Apps werden separat protokolliert](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business),
und berechtigte Workspaces können über unterstützte
[bibliotheksspezifische Endpunkte der Compliance API](https://help.openai.com/en/articles/20001052-library-for-chatgpt) auf aktive Dateien in der Bibliothek zugreifen.
Diese Aufzeichnungen ergeben kein lückenloses Audit-Protokoll für alle Dateivorgänge in der gehosteten Umgebung,
Shell-Befehle, Browserinteraktionen, Tool-Aufrufe oder Genehmigungen.
Prüfe in der nach Anmeldung zugänglichen Dokumentation der Compliance API,
welche Ereignisse und Produkte derzeit abgedeckt sind.

Die Plattform für Compliance-Protokolle bewahrt Daten 30 Tage lang auf. Exportiere Datensätze
kontinuierlich in ein genehmigtes E-Discovery-, Data-Loss-Prevention-, SIEM-
oder Data-Lake-System, wenn deine Organisation eine längere Aufbewahrung benötigt. Weitere Informationen findest du im
[Leitfaden zur OpenAI-Compliance-Plattform](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).

### Lassen sich ungewöhnliches Verhalten, Fehler oder Nutzungsspitzen schnell erkennen?

Workspace-Analysen, Compliance-Protokolle und verbundene Monitoring-Tools helfen
Admins, die Nutzung zu überprüfen und unterstützte Aktivitäten in ChatGPT, Work und Codex
zu untersuchen. Je nach verwendeter Berichtsoberfläche können die Signale aktive Nutzende,
unterstützte Nachrichten, App-Aktivitäten, die Nutzung von Agenten, Authentifizierungs- oder
Administrationsereignisse und den Credit-Verbrauch umfassen. Exportierte Protokolle können
E-Discovery, die Verhinderung von Datenverlust, SIEM, Audits und Untersuchungen unterstützen.
Die Erkennungsqualität hängt von Tarif, Ereignisabdeckung, Zuordnung, Aktualität und
konfigurierten Regeln ab.

Zu den Signalen, die eine Überprüfung rechtfertigen können, gehören ein unerwarteter Anstieg der Nutzung oder des
Credit-Verbrauchs, ungewöhnliche Aktivitäten von Nutzenden oder Agenten, wiederkehrende Betriebsfehler sowie
relevante Authentifizierungs- oder Administrationsereignisse. Prüfe die konkreten Signale anhand der
geltenden Schemata für Analysen, Compliance und Audit-Protokolle.

Für Codex-Aktivitäten stellen Codex-Analysen und die Analytics API unterstützte
Kennzahlen zur Verbreitung und Aktivität bereit. Organisationen, die lokale Codex-Clients verwenden, können
OpenTelemetry-Exporte für Ereignisse wie API-Anfragen, Fehler, Prompt-Metadaten,
Entscheidungen über Tool-Genehmigungen und Tool-Ergebnisse aktivieren. Prompt-Inhalte werden
unkenntlich gemacht, sofern `otel.log_user_prompt = true` nicht separat und ausdrücklich
aktiviert ist. Weitere Informationen findest du unter
[Monitoring und Telemetrie](/de-DE/codex/agent-approvals-security#monitoring-and-telemetry).
Diese lokale Codex-Telemetrie bietet keinen OpenTelemetry-Export
für ChatGPT Work im Web.

## Governance

### Wie können Admins Zugriff, Berechtigungen und Richtlinien steuern?

Governance umfasst drei miteinander verbundene, aber getrennte Ebenen:

- **Zugriffskontrollen für ChatGPT Work** bestimmen, wer ChatGPT Work auf
  der jeweiligen Oberfläche nutzen darf.
- **Kontrollen für Workspace-Agenten** bestimmen, wer wiederverwendbare Agenten und gemeinsam genutzte Verbindungen erstellen, veröffentlichen, teilen,
  zeitlich planen oder konfigurieren darf, sofern
  Workspace-Agenten verfügbar sind.
- **Die verwaltete Konfiguration von Codex** regelt die abgedeckten Aspekte des lokalen Laufzeitverhaltens von Codex
  und konfiguriert gehostetes ChatGPT Work nicht.

Die verwaltete Konfiguration schränkt das Laufzeitverhalten im unterstützten Umfang ein. Sie gewährt keinen
Zugriff auf den Workspace, ersetzt RBAC nicht und entzieht Nutzenden nicht den Zugriff auf den Workspace. Diese
Ebenen bilden keine einheitliche Oberfläche für die Richtlinienverwaltung von ChatGPT Work. Analysen und Compliance-Protokolle
schaffen zusätzliche Transparenz innerhalb ihres dokumentierten Geltungsbereichs für Produkte und
Ereignisse.

Für unterstützte lokale Codex-Clients kann die Enterprise-Administration
[verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration) und
[Berechtigungsprofile](/de-DE/codex/permissions) anwenden. Diese Kontrollen für lokale Clients
gewähren keinen Zugriff auf gehostetes ChatGPT Work und ersetzen nicht die dafür geltenden Workspace-Berechtigungen.

### Lässt sich der Zugriff nach Gruppe, Rolle, Workspace oder Funktion einschränken?

Ja. Bei berechtigten Enterprise- und Edu-Tarifen, die benutzerdefinierte RBAC für Mitglieder
unterstützen, lassen sich die Funktionen von ChatGPT Work über Workspace-Rollen, Identitätsgruppen
und von der Administration festgelegte Berechtigungen eingrenzen. ChatGPT Business nutzt die jeweils geltenden
Kontrollen auf Workspace-Ebene, bietet aber weder benutzerdefinierte RBAC für Mitglieder noch
die Gruppensynchronisierung über SCIM. Weise unterstützte Funktionen entsprechend dem geschäftlichen Bedarf
und den Richtlinien deiner Organisation zu. Weitere Informationen findest du im
[RBAC-Leitfaden](https://help.openai.com/en/articles/11750701-rbac) und in dieser
[RBAC-Anleitung](https://vimeo.com/1207482321/d1286e4467?share=copy&fl=sv&fe=ci).

Wenn benutzerdefinierte RBAC verfügbar ist, können Organisationen damit festlegen, welche
Nutzenden auf ChatGPT Work zugreifen, Workspace-Einstellungen verwalten, genehmigte
Plug-ins konfigurieren oder unterstützte Funktionen von Workspace-Agenten nutzen dürfen. In berechtigten
Enterprise- und Edu-Workspaces können monatliche Nutzungslimits eine schrittweise Einführung unterstützen:
mit Standardlimits für den Workspace und für Gruppen sowie Ausnahmen für einzelne Personen.

Der Zugriff auf verbundene Systeme wird weiterhin unabhängig geregelt. Beschränke Plug-ins,
gemeinsam genutzte Zugangsdaten, Repositories und Aktionen mit Schreibzugriff mithilfe von
Workspace-Berechtigungen, Plug-in-Einstellungen und den Kontrollen des Quellsystems auf den
unbedingt erforderlichen Personenkreis. Bei unterstützten lokalen Codex-Clients kann die verwaltete
Konfiguration lokale Laufzeitfunktionen zusätzlich einschränken. Für gehostetes Work gelten eigene
Kontrollen auf Workspace- und Produktebene.

### Wie werden Laufzeit- und Netzwerkgrenzen geregelt?

Die Sicherheitsgrenzen für ChatGPT Work hängen von der jeweiligen Aufgabe ab. Eine normale Chat-Unterhaltung,
ein Arbeitsablauf mit verbundenen Systemen, eine geplante Aufgabe und ein Codex-Chat können in verschiedenen
Umgebungen mit unterschiedlichen Berechtigungen, Tools und unterschiedlichem Netzwerkzugriff ausgeführt werden.

Steuere jede Ausführungsumgebung über die dafür geltenden Kontrollen. Work Cloud
regelt gehostetes Work auf unterstützten Oberflächen im Web, auf Mobilgeräten und auf dem Desktop.
Work Lokal regelt lokales Work auf dem Desktop, und Codex Lokal steuert den unterstützten lokalen
Codex-Zugriff in Desktop-, CLI- und IDE-Clients. Netzwerkberechtigungen für Browser und Shell
schränken Work Cloud zusätzlich ein. Für Suche, Apps, Plug-ins, verfügbare Workspace-Agenten
und Berechtigungen der Quellsysteme gelten weiterhin getrennte Kontrollen. Die jeweils geltende
verwaltete Konfiguration und lokale Laufzeitrichtlinien regeln ausschließlich die von ihnen
unterstützte lokale Nutzung. Diese Kontrollen sind nicht austauschbar.

Lokale Codex-Ausführungen in der ChatGPT-Desktop-App, der CLI und der IDE erfolgen auf
dem Gerät der jeweiligen Person mit Sandboxing auf Betriebssystemebene und Genehmigungsrichtlinien.
Codex Cloud führt Chats in isolierten, von OpenAI verwalteten Umgebungen aus. Für unterstützte
lokale Clients kann die Enterprise-Administration mit verwalteten Vorgaben
Berechtigungsprofile, Genehmigungen, Dateisystem- und Netzwerkzugriff, MCP-Server,
Hooks, Befehlsregeln und weiteres unterstütztes Laufzeitverhalten einschränken.

## Nutzung und Kosten

<a id="how-does-work-usage-translate-into-spend-over-time"></a>
<a id="how-does-work-mode-usage-translate-into-spend-over-time"></a>

### Wie wirkt sich die Nutzung von ChatGPT Work im Laufe der Zeit auf die Kosten aus?

[Für ChatGPT Work und Codex gelten dieselben Preise, Credits und Nutzungslimits](/de-DE/codex/pricing).
Prüfe bei dafür infrage kommenden Vereinbarungen auf Credit-Basis die gesamte Chat- und Work-Nutzung
der Beschäftigten im Verhältnis zum gemeinsamen Credit-Kontingent des Workspace. Der Verbrauch hängt
vom Modell, den jeweiligen Einstellungen für Reasoning-Aufwand oder Geschwindigkeit, den verarbeiteten Ein- und Ausgaben
sowie den jeweils berücksichtigten Tools oder Funktionen ab.

Die Nutzung vertraglich vereinbarter Credits erhöht deinen Rechnungsbetrag nicht automatisch. Die tatsächlichen
Kosten hängen vom verbleibenden Credit-Guthaben, den vertraglich vereinbarten Preisen und davon ab,
ob dein Konto für Mehrverbrauch berechtigt ist und welches Überschreitungslimit für den Workspace konfiguriert ist. Beispiele für die Planung,
Informationen zu den tatsächlich geltenden Limits pro Person, den Grenzen der Berichterstattung und Details zur Abrechnung
findest du unter [ChatGPT Work: Nutzung und Kosten](/de-DE/codex/enterprise/chatgpt-work-usage-and-cost).

Die größten Schwankungen treten häufig bei Arbeitsabläufen auf, die oft ausgeführt werden,
große Informationsmengen abrufen oder verarbeiten, mehrere Tools oder Apps aufrufen,
nach Fehlern weitere Versuche starten oder große Artefakte erzeugen. Besonders kostenrelevant sind
geplante oder wiederkehrende Aufgaben, große Dateien, umfangreiche Abrufe aus
Unternehmensquellen, wiederholte App-Aufrufe sowie Codex-Chats, die Repositories
verarbeiten, Befehle ausführen oder Cloud-Umgebungen nutzen. Sofern verfügbar, können
auch Trigger der Workspace Agent API den Verbrauch erhöhen.

Überwache diese Muster im Zeitverlauf mit Ausgabenkontrollen, Nutzungsanalysen und Berichten.
Prüfe die Nutzung anhand der in der aktuellen Analyseoberfläche unterstützten Dimensionen und
passe Limits oder den Umfang der Einführung an den geschäftlichen Nutzen an. Betrachte
aggregierte Analysedaten nicht als genaue Zuordnung der Kosten zu einzelnen Arbeitsabläufen.

Workspace-Analysen, Compliance-Protokolle und verbundene Monitoring-Tools können der Administration helfen,
die Nutzung zu prüfen und unterstützte Aktivitäten zu untersuchen. Ob sich riskantes oder ungewöhnliches
Verhalten erkennen lässt, hängt vom Tarif, der Protokollabdeckung, der Zuordnung,
der Aktualität der Daten und den in deinen Monitoring-Systemen konfigurierten Regeln ab.

### Welche Nutzungslimits, Warnmeldungen oder Obergrenzen stehen zur Verfügung?

Berechtigte Enterprise- und Edu-Workspaces können monatliche Limits pro Person und
Ausgabenkontrollen für den gesamten Workspace für die Nutzung auf Credit-Basis einsetzen:

- **Verbrauch von Credits überwachen:** Prüfe die unterstützten Berichte zur Nutzung von Credits in der
  Global Admin Console und in den Workspace-Einstellungen.
- **Monatliches Standardlimit festlegen:** Lege für den Workspace ein Standardlimit für Credits
  pro Person fest.
- **Gruppenspezifische Limits anwenden:** Lege für Gruppen monatliche Standardlimits pro Person fest, die
  ihren Arbeitsabläufen, Zuständigkeiten oder der Einführungsphase entsprechen.
- **Ausnahmen für einzelne Personen festlegen:** Lege für eine bestimmte Person ein abweichendes Limit fest, ohne
  den Standardwert für die gesamte Gruppe zu ändern.
- **Anträge auf Erhöhung prüfen:** Wenn Anträge aktiviert sind, können Nutzende ein
  höheres Monatslimit beantragen. Bei Genehmigung wird eine Ausnahme für die betreffende Person angelegt.
- **Mögliche Gesamtausgaben des Workspace steuern:** Konfiguriere Warnmeldungen zu Credits für den Workspace und
  das Überschreitungslimit separat in der Global Admin Console. Warnmeldungen informieren
  die vorgesehenen Personen; das Überschreitungslimit regelt die zulässige Nutzung, sobald das vertraglich vereinbarte
  Credit-Kontingent aufgebraucht ist.
- **Nutzungsdaten exportieren:** Berechtigte Personen mit Enterprise-Adminrechten können über
  die einheitliche Cost API auf Daten zur Nutzung von Credits für interne Berichte oder
  das Monitoring zugreifen.

Nutzende können ihre eigene Nutzung einsehen und, falls die Funktion aktiviert ist, weitere Credits beantragen,
aber zugewiesene Limits nicht ändern. Weitere Informationen findest du unter
[Nutzungslimits und Überschreitungen verwalten](https://help.openai.com/en/articles/20001001-manage-usage-limits-and-overages-in-chatgpt-enterprise-and-edu)
sowie in der
[Anleitung zu Ausgabenkontrollen](https://vimeo.com/1207484127/0f2029dd01?share=copy&fl=sv&fe=ci).

## Maßnahmen bei Vorfällen und zur Zugriffsaufhebung

### Wie kann die Administration Zugriffe oder Aktivitäten unterbinden?

Wenn Nutzende entfernt oder Vorfälle untersucht werden, muss die Administration unter Umständen
Zugriffe sperren, Apps deaktivieren, gemeinsam genutzte Zugangsdaten widerrufen,
geplante Aufgaben pausieren oder Codex-Zugangsdaten widerrufen.

Für die Zugriffsaufhebung gibt es unter anderem folgende Möglichkeiten:

- Entziehe der betreffenden Person den Zugriff auf den Workspace oder die Gruppe. Bei über SCIM
verwalteten Konten musst du den Zugriff beim Identitätsanbieter entziehen; andernfalls kann das Konto
bei einer späteren Synchronisierung erneut bereitgestellt werden.
- Deaktiviere oder beschränke das betreffende Plug-in oder die betreffende App.
- Entziehe einer gemeinsam genutzten Verbindung, einem Bot oder einem Dienstkonto über die jeweils
zuständige Oberfläche den Zugriff. Workspace-Verantwortliche und Personen mit Adminrechten können
Codex-Workspace-Zugriffstoken separat widerrufen.
- Ziehe die Veröffentlichung eines Workspace-Agenten zurück oder lass ihn von der für ihn verantwortlichen Person
oder der Workspace-Administration löschen.
- Deaktiviere die betreffende geplante Aufgabe oder, sofern verfügbar, den Trigger
der Workspace Agent API.
- Widerrufe für den Codex-Zugriff jeweils separat das betreffende Zugriffstoken,
die Repository-Verbindung und den Zugriff auf die Cloud-Umgebung. Über die verwaltete Konfiguration
lassen sich Zugriffe nicht entziehen.

## Weitere Ressourcen für deine Teams

| Thema                    | Verwende die Ressource, wenn du Folgendes erklärst                                                      | ChatGPT-Lernseite                                               |
| ------------------------ | ----------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Übersicht zu Work            | Wie die Ausführung in der Cloud, Browserzugriff, Netzwerkrichtlinien und Datengrenzen funktionieren | [Übersicht zu ChatGPT Work](/de-DE/codex/enterprise/chatgpt-work-overview) |
| Workspace-Setup und RBAC | Wer Codex nutzen und verwalten kann                                              | [Leitfaden für den administrativen Rollout](/de-DE/codex/enterprise/admin-setup)             |
| Authentifizierung           | Wie sich die Anmeldung bei ChatGPT, die Anmeldung mit API-Schlüssel und die Workspace-Richtlinie unterscheiden             | [Authentifizierung](/de-DE/codex/auth)                                    |
| Genehmigungen und Sandboxing | Wie Codex Datei-, Befehls- und Netzwerkaktionen sowie Toolaktionen mit Seiteneffekten steuert    | [Genehmigungen und Sicherheit für Agenten](/de-DE/codex/agent-approvals-security)  |
| Verwaltete Richtlinie           | Wie die Administration Codex-Einstellungen durchsetzt, die Nutzende nicht überschreiben können                        | [Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration) |
| Laufzeitumgebungen     | Wie Setup, Secrets, Caches und Aufgabenphasen in Codex Cloud funktionieren                  | [Cloud-Umgebungen](/de-DE/codex/environments/cloud-environment)      |
| Internetzugang          | Wie Domain-Zulassungslisten und HTTP-Methoden in Codex Cloud funktionieren                       | [Internetzugang für Agenten](/de-DE/codex/cloud/internet-access)            |
| Berechtigungen              | Wie Dateisystem- und Netzwerkkontrollen sowie das Sperren von Lesezugriffen funktionieren                          | [Berechtigungen](/de-DE/codex/permissions)                                |
| Beobachtbarkeit            | Wie Analysen, Berichterstattung und Compliance-Exporte funktionieren                         | [Governance](/de-DE/codex/enterprise/governance)                       |
| Zugangsdaten für Automatisierungen   | Wie Zugriffstoken erstellt, eingeschränkt, widerrufen und geprüft werden                  | [Zugriffstoken](/de-DE/codex/enterprise/access-tokens)                 |

## Handlungsempfehlungen für die Administration

- **Lege fest, wer zuerst Zugriff erhalten soll.** Entscheide, ob du den Zugriff auf
  ChatGPT Work einschränken, eine Pilotphase starten oder ChatGPT Work umfassend einführen möchtest. Viele Organisationen beginnen
  mit erfahrenen Nutzenden, internen Schlüsselpersonen oder Teams mit klaren Anwendungsfällen.
- **Prüfe Rollen und Berechtigungen.** Sieh unter **Berechtigungen und Rollen** nach, welche
  Nutzenden oder Gruppen auf ChatGPT Work zugreifen können. Berücksichtige beim Zugriff den geschäftlichen Bedarf, den Vorbereitungsstand
  und die Erwartungen an die Governance.
- **Prüfe Plug-ins und Datenquellen.** ChatGPT Work ist am nützlichsten, wenn es freigegebene
  geschäftliche Informationen aus Dateien, E-Mails, Kalendern, Slack oder CRM nutzen kann. Prüfe
  die aktivierten Plug-ins, ihre Zielgruppen und ob die App-Richtlinien weiterhin dazu passen, wie Nutzende
  Aufgaben delegieren sollen.
- **Kommuniziere klar, welche Anwendungsfälle geeignet sind.** Empfiehl ChatGPT Work für mehrstufige
  Aufgaben mit höherem Nutzen, etwa für Recherche, das Zusammenführen und Analysieren von Informationen, das Erstellen von Dateien,
  das Aktualisieren von Arbeitsabläufen und das Erstellen wiederverwendbarer Ergebnisse. Nutze Chat für kurze Fragen,
  kleinere Textüberarbeitungen oder Brainstorming.
- **Prüfe die Einstellungen für Credits und Nutzung.** Da ChatGPT Work länger laufende
  Aufgaben ausführen kann, kann es mehr Credits verbrauchen als eine gewöhnliche Unterhaltung in Chat. Prüfe
  Standardwerte, gruppenspezifische Standardwerte, abweichende Einstellungen für einzelne Nutzende und interne Leitlinien dazu,
  wie der Aufwand am geschäftlichen Nutzen ausgerichtet werden soll.
- **Wähle für den Einstieg Arbeitsabläufe mit hohem Nutzen aus.** Beginne mit klaren, überprüfbaren
  Ergebnissen wie Kundenbriefings, regelmäßigen Berichten, Zusammenfassungen von Rechercheergebnissen,
  Aktualisierungen von Trackern oder sorgfältig ausgearbeiteten Dokumenten und Folien.
- **Bereite interne Schlüsselpersonen und Supportteams vor.** Stelle internen Schlüsselpersonen, Training Leads
  und Supportteams zuerst Ressourcen für die Einführung bereit, damit sie Fragen beantworten,
  Feedback sammeln und beispielhaft zeigen können, wie sich Aufgaben effektiv delegieren lassen.
- **Kommuniziere klar, welche Überprüfungen und Genehmigungen erwartet werden.** Erinnere Nutzende daran, dass Menschen
  weiterhin dafür verantwortlich sind, Ergebnisse zu überprüfen, wichtige Aussagen zu validieren und
  Aktionen mit erheblichen Auswirkungen zu genehmigen, bevor die Ergebnisse geteilt oder genutzt werden.
- **Beobachte die Akzeptanz und passe dein Vorgehen an.** Prüfe nach der Einführung die Nutzung, das Feedback, den Verbrauch von Credits
  und die delegierten Aufgaben. Nutze die Erkenntnisse, um den Zugriff,
  die Leitlinien, die Schulungen und die Ausweitung der Nutzung anzupassen.

<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/user-lifecycle -->

Dieser Leitfaden zeigt dir, wie du Mitarbeitenden beim Eintritt den passenden Zugriff auf den ChatGPT-Workspace gewährst, ihn bei geänderten Aufgaben anpasst und beim Austritt entziehst. Der Prozess umfasst außerdem Workspace-Plätze, gruppenbasierte Rollen, Codex-Zugriffstoken und angebundene Systeme mit eigenen Zugriffskontrollen.

Single Sign-on (SSO) überprüft die Identität von Mitarbeitenden. Bei der Provisionierung werden sie einem Workspace hinzugefügt. Keine der beiden Aktionen allein bestimmt ihren Platz, ihre Funktionsberechtigungen, die Richtlinie für ihre lokale Laufzeit oder ihren Zugriff auf ein externes System.

Verwalte den Zugriff von Mitarbeitenden in drei Phasen:

- **Eintritt:** Richte den Workspace-Zugriff, Gruppen, Rollen und den passenden Platz ein.
- **Wechsel:** Aktualisiere die Gruppenmitgliedschaften der Person und entferne nur nicht mehr benötigte, direkt zugewiesene Rollen.
- **Austritt:** Entziehe den Workspace-Zugriff, widerrufe Token und überprüfe angebundene Systeme.

## Voraussetzungen prüfen und Verantwortliche festlegen

Kläre vor dem Onboarding von Mitarbeitenden, wer für welchen Teil des Lebenszyklus zuständig ist:

| Verantwortliche Person                     | Zuständigkeit                                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------------- |
| Person mit Inhaberrolle im Workspace           | Verzeichnissynchronisierung aktivieren, Workspace-Rollen zuweisen, Platztypen genehmigen und Audit-Zugriff überprüfen |
| Für die Identitätsadministration zuständige Person    | Identitätsanbieter, Anwendungszuweisungen, Provisionierungsgruppen und Synchronisierungsstatus konfigurieren        |
| Person mit Administrationsrolle im Workspace   | Workspace-Mitglieder, Gruppenmitgliedschaften und unterstützte Verwaltungseinstellungen überprüfen                     |
| Für Sicherheit oder den Dienst verantwortliche Person | Codex-Token, angebundene Systeme, gemeinsam genutzte Automatisierungen und erforderliche Audit-Nachweise überprüfen                |

Bestätige den Ziel-Workspace, verifiziere bei Bedarf die E-Mail-Domain der Organisation und bestimme eine Person mit Inhaberrolle im Workspace, die die Verzeichnissynchronisierung aktivieren kann. Prüfe anschließend, welche Einstellungen der Workspace-Tarif unterstützt:

| Funktion                                 | Unterstützte Workspace-Tarife                                                                                    |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| Verzeichnissynchronisierung über SCIM     | ChatGPT Enterprise, Edu und Healthcare                                                                      |
| Benutzerdefinierte Rollen und rollenbasierte Zugriffskontrolle | ChatGPT Enterprise, Edu, Healthcare und Teachers                                                            |
| Codex-Zugriffstoken                        | ChatGPT Business und Enterprise                                                                              |
| Reine Codex-Plätze                           | Berechtigte Enterprise-Workspaces und bestehende Business-Workspaces, die die Voraussetzungen erfüllen; nicht für Edu, Teachers oder Healthcare verfügbar |

SCIM steht für System for Cross-domain Identity Management. Ein Business-Workspace kann Codex-Zugriffstoken ohne SCIM unterstützen, während ein Edu-Workspace SCIM ohne Codex-Zugriffstoken oder reine Codex-Plätze unterstützen kann. Verwende nur die Einstellungen, die in deinem Workspace verfügbar sind.

Ein Business-Workspace kann reine Codex-Plätze nur behalten und hinzufügen, wenn er vor dem 24. Juni 2026
bereits einen Codex-Platz hatte oder zu diesem Stichtag eine ausstehende Einladung für einen Codex-Platz
vorlag, die die Voraussetzungen erfüllte. Neue Business-Workspaces und Workspaces ohne entsprechenden Platz
oder entsprechende Einladung können keinen ersten reinen Codex-Platz hinzufügen. Siehe
[Workspace-Lebenszyklus und Migration in ChatGPT Business verwalten](https://help.openai.com/en/articles/8801890-managing-workspace-lifecycle-and-migration-in-chatgpt-business).

Wenn der Workspace mehrere Platztypen unterstützt, überprüfe die Standardeinstellung unter
**Workspace-Einstellungen \> Identität & Zugriff** , bevor du die automatische
Provisionierung aktivierst. Über SCIM provisionierte Konten übernehmen diese Standardeinstellung. Der Platz bestimmt,
welche Produktbereiche verfügbar sind. Eine benutzerdefinierte Rolle kann keinen Zugriff gewähren,
der nicht im Platz enthalten ist.

Prüfe unter **Berechtigungen & Rollen** die Einstellungen für lokalen Zugriff, Zugriffstoken,
die Gültigkeitsdauer von Zugangsdaten und Remote-Geräte. Einige Workspaces bündeln den lokalen Zugriff
unter **Codex und Work Lokal** mit der Einstellung **Mitgliedern die lokale Nutzung von Codex und
Work erlauben** . Andere trennen **Codex Lokal** mit **Mitgliedern die lokale Nutzung
von Codex erlauben** von **Work Lokal** mit **Work lokal nutzen**.
Separate Einstellungen für Codex und Work gewähren jeweils keinen Zugriff auf das andere Produkt. Die Einstellungen
für Token befinden sich entweder im Abschnitt für lokalen Zugriff oder in einem separaten **Abschnitt
„Zugriffstoken“** . Diese Einstellungen sind unabhängig von Gruppenmitgliedschaften und
zugewiesenen Platztypen.

Das folgende Beispiel zeigt die gemeinsamen Einstellungen für **Codex und Work Lokal** und einen
separaten Abschnitt **Zugriffstoken** :

  

Aktuelle Voraussetzungen und unterstützte Identitätskonzepte findest du unter
[Identität und Provisionierung](https://help.openai.com/en/articles/9672121)
und [Mitglieder, Platztypen, Rollen und Zugriff verwalten](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise).

## Festlegen, wie Mitarbeitende dem Workspace beitreten

Wähle für jede Zielgruppe eine primäre Provisionierungsmethode:

| Methode                     | So wird Zugriff gewährt                                                       | Hier wird Zugriff entzogen                                  |
| -------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------- |
| Manuelle Einladung          | Eine Person mit Inhaber- oder Administrationsrolle im Workspace lädt Mitarbeitende ein                          | Mitgliederverwaltung des Workspace                         |
| Automatische Kontoerstellung | Mitarbeitende mit einer zulässigen E-Mail-Domain melden sich an                      | Workspace-Verwaltung und der entsprechende Identitätsprozess |
| Verzeichnissynchronisierung mit SCIM   | Die für die Identitätsadministration zuständige Person weist Mitarbeitende beim Identitätsanbieter zu | Die Anwendung oder Provisionierungsgruppe beim Identitätsanbieter |

Verwende manuelle Einladungen für einen kleinen Pilotversuch oder eine Gruppe, die nicht über die Verzeichnissynchronisierung verwaltet wird. Verwende SCIM, wenn sich die Workspace-Mitgliedschaft bei Eintritt, Teamwechsel oder Austritt von Mitarbeitenden nach den Zuweisungen beim Identitätsanbieter richten soll.

Aktiviere die automatische Kontoerstellung und SCIM nicht gleichzeitig. Konten, die über
die automatische Kontoerstellung hinzugefügt werden, werden möglicherweise nicht über SCIM verwaltet. Wenn du sie aus
einer Gruppe beim Identitätsanbieter entfernst, kann ihr Workspace-Zugriff daher bestehen bleiben. In den
[häufigen Fragen zur SCIM-Integration](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
findest du aktuelle Hinweise.

Je nach genehmigtem Identitäts-Setup kann SCIM einen einzelnen ChatGPT-Workspace oder den Mandanten einer Organisation anbinden. Lege jede Workspace- und Produktzuweisung ausdrücklich fest. Eine gemeinsame Verzeichnisanbindung gewährt oder entzieht nicht automatisch den Zugriff auf jeden Workspace oder jede Organisation der API-Plattform.

## Eine Provisionierungsgruppe mit dem richtigen Workspace verbinden

Konfiguriere die Verbindung, bevor du die erste am Pilotversuch teilnehmende Person hinzufügst. Die Person mit Inhaberrolle im Workspace und die für die Identitätsadministration zuständige Person haben unterschiedliche Aufgaben:

1. Lass die Person mit Inhaberrolle im Workspace den vorgesehenen ChatGPT-Workspace auswählen und
**Workspace-Einstellungen \> Gruppen** überprüfen. Dokumentiere bestehende Gruppennamen, Mitglieder,
   Zuweisungen benutzerdefinierter Rollen und relevante Projekt- oder GPT-Freigaben.
2. Lass die für die Identitätsadministration zuständige Person die genaue Gruppe beim Identitätsanbieter bestimmen, die synchronisiert werden soll. Vergleiche ihren Namen und ihre Mitglieder mit allen bestehenden Workspace-Gruppen.
3. Wenn eine synchronisierte Gruppe denselben Namen wie eine bestehende Workspace-Gruppe hat, gleiche die betroffene Gruppe ab oder benenne sie um, bevor du die Synchronisierung aktivierst. Lass die Person mit Inhaberrolle im Workspace die daraus resultierende Mitgliederliste, die geerbten Rollen und die Freigaben genehmigen. Eine bestehende Gruppe mit übereinstimmendem Namen wird über SCIM verwaltet, und ihre Mitgliedschaften werden dann vom Identitätsanbieter gesteuert.
4. Wähle eine eng abgegrenzte Pilotgruppe aus und dokumentiere den genehmigten Workspace, die erwarteten Mitarbeitenden und die Zuweisungen von Rollen zu Gruppen.
5. Lass die Person mit Inhaberrolle im Workspace **Workspace-Einstellungen \> Identität & Zugriff** öffnen
   und **Verzeichnissynchronisierung aktivieren** auswählen. Wenn du dazu aufgefordert wirst, wähle für die Provisionierung auf Workspace-Ebene **SCIM nur
   für diesen Workspace verwenden** oder für die genehmigte Provisionierung auf Mandantenebene **Option zur Erweiterung
   auf weitere Produkte beibehalten** . Wenn
   SCIM auf Mandantenebene bereits aktiv ist, verwalte die bestehende Verbindung,
   anstatt eine zweite Workspace-Verbindung anzulegen.
6. Lass die für die Identitätsadministration zuständige Person die Verbindung zum Identitätsanbieter fertig einrichten, die ChatGPT-Anwendung auswählen und die genehmigte Gruppe zuweisen, um Mitglieder im vorgesehenen Workspace zu provisionieren.
7. Prüfe unter **Workspace-Einstellungen \> Gruppen**, ob die ausgewählte Gruppe
   ihre SCIM-Kennzeichnung anzeigt. Überprüfe den Gruppennamen, die synchronisierten Mitglieder und den Ziel-Workspace,
   bevor du die Gruppe für den Zugriff verwendest.
8. Bitte die Person mit Inhaberrechten im Workspace, **Berechtigungen & Rollen \> Benutzerdefinierte Rollen** zu öffnen,
   die genehmigte Rolle zu erstellen oder auszuwählen und sie der synchronisierten Gruppe zuzuweisen.
   Die Rollenkonfiguration ist im Web verfügbar und erfordert
   Inhaberrechte im Workspace.
9. Prüfe die effektiven Berechtigungen der Gruppe und den standardmäßig zugewiesenen Platztyp im Workspace,
bevor du eine für die Zielgruppe repräsentative Person zum Pilottest hinzufügst.

Die Administration des Identitätsanbieters verwaltet die Anwendungszuweisungen und Gruppenmitgliedschaften.
Die Person mit Inhaberrechten im Workspace verwaltet die Verzeichnissynchronisierung
und die Rollenzuweisungen im Workspace. In den [häufigen Fragen zur SCIM-Integration](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
und unter [Rollenbasierte Zugriffskontrolle konfigurieren](https://help.openai.com/en/articles/11750701-rbac)
findest du die aktuellen anbieterspezifischen Schritte und Angaben zur Verfügbarkeit.

## Zugang für neue Beschäftigte bereitstellen

Für eine über SCIM verwaltete Person:

1. Bestätige den vorgesehenen Workspace, die verifizierte E-Mail-Adresse, den standardmäßig zugewiesenen Platztyp
und die Gruppe beim Identitätsanbieter.
2. Weise die Person beim Identitätsanbieter der ChatGPT-Anwendung oder einer Gruppe zu,
die Zugriff gewährt.
3. Warte, bis die Verzeichnissynchronisierung abgeschlossen ist. Prüfe den aktuellen
Status beim Identitätsanbieter, falls die Person nicht angezeigt wird.
4. Prüfe unter **Workspace-Einstellungen \> Mitglieder** die E-Mail-Adresse der Person,
   ihre Mitgliedschaft oder ausstehende Einladung, den Platztyp und die SCIM-Kennzeichnung.
5. Prüfe unter **Workspace-Einstellungen \> Gruppen**, ob die Person der
   vorgesehenen synchronisierten Gruppe angehört. Lass die Person mit Inhaberrechten im Workspace
   die benutzerdefinierte Rolle überprüfen, die dieser Gruppe zugewiesen ist.
6. Bitte eine für die Zielgruppe repräsentative Person, sich im richtigen Workspace anzumelden
und die benötigten Produktoberflächen, Funktionen und verbundenen Systeme zu prüfen.
7. Dokumentiere gemäß dem genehmigten Verfahren deiner Organisation, wer für den Zugriff verantwortlich ist
und dass die Überprüfung erfolgreich war.

Wenn du eine Person manuell hinzufügst, sende die Einladung über die Mitgliederverwaltung des Workspace.
Führe anschließend dieselben Prüfungen für Platz, Gruppe, Rolle und Anmeldung durch.

Eine Gruppe organisiert Mitglieder, gewährt aber allein noch keinen Zugriff auf jede Funktion.
Das aktuelle Verfahren zur Rollenzuweisung findest du unter
[Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions)
und [Rollenbasierte Zugriffskontrolle konfigurieren](https://help.openai.com/en/articles/11750701-rbac).

## Zugriff bei einem Teamwechsel aktualisieren

Bei einem Teamwechsel können Beschäftigte den Zugriff aus bisherigen Gruppen- oder Rollenzuweisungen behalten.
Aktualisiere die Mitgliedschaft im dafür zuständigen Quellsystem, bevor du
den neuen Zugriffsumfang überprüfst:

1. Ermittle das neue Team der Person, den benötigten Workspace und Platz,
die genehmigten Funktionsberechtigungen und die Zielgruppe.
2. Füge die Person zuerst der genehmigten Zielgruppe hinzu und entferne sie erst danach
aus ihrer bisherigen Gruppe, wenn sie während des gesamten Wechsels im Workspace bleiben muss.
Aktualisiere über SCIM verwaltete Mitgliedschaften beim Identitätsanbieter und
manuell verwaltete Mitgliedschaften über die Workspace-Verwaltung.
3. Bestätige, dass die genehmigte Rolle der Zielgruppe bereits zugewiesen ist.
Behalte bestehende Rollenzuweisungen gemeinsam genutzter Gruppen bei,
damit die anderen Mitglieder ihren genehmigten Zugriff behalten.
4. Lass eine Person mit Inhaberrechten im Workspace die Rollenzuweisung einer Gruppe erst ändern,
nachdem sie eine separate Richtlinienänderung für die gesamte Gruppe genehmigt
und deren Auswirkungen auf jedes Mitglied geprüft hat.
5. Bitte eine Person mit Inhaberrechten im Workspace, das Profil der betreffenden Person zu öffnen, **Direkte Rollen** zu prüfen
   und veraltete, direkt zugewiesene Rollen zu entfernen. Benutzerdefinierte Rollen verwenden die Einstellungen **Standard**,
**Ein** und **Aus**. Ein ausdrücklich gesetztes **Aus** in einer zugewiesenen Rolle hat Vorrang vor
**Ein** in einer anderen Rolle.
6. Prüfe die effektiven Berechtigungen der Person aus allen direkt und über Gruppen
zugewiesenen Rollen, bevor du den Teamwechsel genehmigst.
7. Wenn der Workspace mehrere Platztypen unterstützt, bitte eine Person mit Inhaberrechten im Workspace,
**Workspace-Einstellungen \> Mitglieder \> Platztyp ändern** zu öffnen und zu prüfen,
   welchen Produktzugriff die betreffende Person erhalten soll.
8. Bestätige vor der Umwandlung eines ChatGPT-Platzes in einen reinen Codex-Platz,
dass die Person den Zugriff auf Chats, Erinnerungen, Projekte und andere
ChatGPT-Funktionen verlieren soll. Die zugrunde liegenden Daten werden nicht gelöscht und sind wieder verfügbar,
wenn die Person erneut einen ChatGPT-Platz erhält.
9. Prüfe nach Abschluss der Synchronisierung und der Berechtigungsänderungen sowohl die
neu erlaubten Aktionen als auch die Aktionen, die nicht mehr verfügbar sein sollen.

Wenn die Person für einen Automatisierungsablauf verantwortlich ist, prüfe, ob dessen Codex-Token,
Eintrag im Secret-Manager oder Autorisierung für einen verbundenen Dienst auf eine andere
autorisierte Person übertragen werden sollte. Der Entzug der Berechtigung zur lokalen Nutzung von Codex setzt die
Codex-Token der Person aus, widerruft sie aber nicht. Wird die Berechtigung wiederhergestellt,
werden diese Token erneut aktiviert. Widerrufe daher Anmeldedaten, die dauerhaft keinen Zugriff mehr ermöglichen dürfen.

## Ausscheidende Beschäftigte entfernen

Beginne mit dem System, das die Workspace-Mitgliedschaft der Person verwaltet:

1. Stelle fest, ob die Person über SCIM verwaltet wird oder von der Administration
manuell hinzugefügt wurde.
2. Entferne bei einer über SCIM verwalteten Person deren Zuweisung zur ChatGPT-Anwendung
und entferne sie beim Identitätsanbieter aus allen Bereitstellungsgruppen,
die Zugriff gewähren. Entferne nicht die gemeinsam genutzten Gruppen selbst.
3. Lass eine Person, die nicht über SCIM verwaltet wird, von jemandem mit Inhaber- oder Administrationsrechten im Workspace
   unter **Workspace-Einstellungen \> Mitglieder** entfernen.
4. Bestätige, dass das Mitglied nicht mehr im vorgesehenen Workspace vorhanden ist.
Prüfe bei über SCIM verwaltetem Zugriff, ob die Synchronisierung abgeschlossen ist und keine
andere Zuweisung beim Identitätsanbieter die Mitgliedschaft wiederherstellen kann.
5. Dokumentiere die abgeschlossene Entfernung und benenne eine verantwortliche Person,
die Token, verbundene Systeme und aufbewahrte Daten überprüft.

Verlasse dich nicht allein auf die Entfernung im Workspace, wenn die Person beim Identitätsanbieter weiterhin
einer über SCIM verwalteten Gruppe zugewiesen ist. Eine spätere Synchronisierung kann die
Person wieder zum Workspace hinzufügen.

### Codex-Zugriffstoken widerrufen und Automatisierungen übertragen

Eine Person aus dem Workspace zu entfernen, ersetzt nicht die gezielte Prüfung der Anmeldedaten,
die vertrauenswürdige Automatisierungen verwenden. Wende dieses Verfahren nur an, wenn der
Workspace Codex-Zugriffstoken unterstützt und diese aktiviert sind.

Der Entzug der Berechtigung zur lokalen Nutzung von Codex setzt bestehende Token aus, widerruft sie aber nicht.
Diese Token können wieder funktionieren, wenn eine Person mit Inhaberrechten im Workspace die Berechtigung wiederherstellt.
Widerrufe daher ausdrücklich alle Anmeldedaten, die dauerhaft keinen Zugriff mehr ermöglichen dürfen.

Die Seite **Zugriffstoken** zeigt für jeden Token an, wer ihn erstellt hat und welchen Status er hat. Mit
**Widerrufen** entziehst du aktiven Token den Zugriff:

  

1. Bitte eine Person mit Inhaber- oder Administrationsrechten im Workspace,
[Zugriffstoken](https://chatgpt.com/admin/access-tokens) zu öffnen.
2. Ermittle die Token, die die ausscheidende Person erstellt hat, und die Arbeitsabläufe,
die diese Token verwenden.
3. Wähle die Identität für den Ersatz aus. Nutze für einen dauerhaft ohne menschliche Identität betriebenen Ablauf
   in einem dafür berechtigten Tarif mit nutzungsbasierter Abrechnung ein genehmigtes [dediziertes
   Dienstkonto](/de-DE/codex/enterprise/service-accounts). Bestimme andernfalls ein
   autorisiertes, aktives Mitglied, das die Verantwortung für den Ablauf übernimmt. Lass eine Person mit Inhaberrechten im Workspace diesem Mitglied
   bei Bedarf die Berechtigung zum Erstellen von Zugriffstoken erteilen und bestätige, dass es
   die Berechtigung zur lokalen Nutzung von Codex hat.
4. Erstelle den Ersatz-Token. Eine zur Bedienung des Dienstkontos berechtigte Person kann
   auf dessen Detailseite einen Token erstellen. Soll der Ersatz über eine persönliche Identität erfolgen,
   lass die neue für den Ablauf verantwortliche Person einen Token für ihre eigene
   Identität im ChatGPT-Workspace erstellen. Wenn der Dialog **Berechtigungsbereiche** anzeigt, wähle
**Codex** aus. Wähle weitere Berechtigungsbereiche nur aus, wenn der Ablauf sie benötigt.
   Ein Dialog ohne **Berechtigungsbereiche** erstellt einen reinen Codex-Token. Auch mit Administrationsrechten ist es nicht möglich,
   einen persönlichen Token im Namen einer anderen Person zu erstellen.
5. Aktualisiere das für den Ablauf gespeicherte Secret und prüfe anschließend,
ob der Ablauf mit dem Ersatz-Token erfolgreich ausgeführt wird.
6. Lass die Person mit Inhaber- oder Administrationsrechten im Workspace die Token der ausscheidenden Person
und alle ersetzten Anmeldedaten widerrufen.
7. Bestätige, dass mit den widerrufenen Token keine neuen authentifizierten Ausführungen mehr gestartet werden können.

Wenn eine autorisierte Person den Ablauf übernimmt und einen Token erstellt, verwende einen aussagekräftigen Namen für den Ablauf
und wähle die kürzeste Gültigkeitsdauer für Anmeldedaten, die die Richtlinie deiner Organisation
zulässt. Wenn **Berechtigungsbereiche** angezeigt wird, wähle **Codex** aus und vermeide Berechtigungen,
die der Ablauf nicht benötigt. Das folgende Beispiel zeigt die Oberfläche mit Berechtigungsbereichen:

  

Personen mit Inhaber- oder Administrationsrechten können jeden Token in ihrem Workspace widerrufen. Ein Mitglied
mit der Berechtigung für Zugriffstoken kann nur selbst erstellte Token widerrufen. Informationen zu den aktuellen
Token-Berechtigungen und den Schritten zur Rotation findest du unter
[Zugriffstoken](/de-DE/codex/enterprise/access-tokens#rotate-or-revoke-a-token).

### Verbundene Systeme und aufbewahrte Daten überprüfen

Die Bereitstellung des Workspace-Zugangs regelt nicht sämtliche Zugriffsberechtigungen. Bitte die
für den jeweiligen Dienst verantwortliche Person, den Zugriff auf Folgendes zu prüfen:

- Quellcode-Repositories und verbundene GitHub-Konten.
- Google Drive, Slack und andere verbundene Anwendungen.
- Installierte Plug-ins, mitgelieferte Skills und über Konnektoren bereitgestellte Funktionen.
- Gehostete Codex-Umgebungen, gemeinsam genutzte Automatisierungen und gespeicherte Secrets.
- Verwaltete Geräte, lokal gespeicherte Anmeldedaten und unterstützte Remote-Sitzungen.
- Separate Organisationen, Projekte und API-Schlüssel der API-Plattform.

Nutze die jeweiligen Kontrollmöglichkeiten der einzelnen Systeme. Gehe nicht davon aus, dass eine Änderung an einer Workspace-Gruppe
oder über SCIM die Berechtigungen überall aktualisiert. Unter
[Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions)
findest du das vollständige Modell der Berechtigungsgrenzen. Unter [Kontrollen für Plug-ins](/de-DE/codex/enterprise/apps-and-connectors)
findest du Informationen zur Verfügbarkeit von Plug-ins, zu mitgelieferten Skills und zu Berechtigungen verbundener Apps.

Den Workspace-Zugriff zu entziehen, ist nicht dasselbe wie Inhalte zu löschen. Wenn ein Mitglied
ausscheidet, überträgt der Workspace die Inhaberschaft an dessen Projekten und individuellen
GPTs automatisch auf eine Person mit Inhaberrechten im Workspace. Diese Inhalte werden nicht zur Löschung vorgemerkt.
Wenn das Mitglied wieder beitritt, erhält es die Inhaberschaft zurück.

In Enterprise- und Edu-Workspaces unterliegen Chats, Dateien und Canvas-Dokumente
der konfigurierten Aufbewahrungsrichtlinie des Workspace. Business-Workspaces bewahren Chats,
Dateien und Canvas-Dokumente unbegrenzt auf. Healthcare-Workspaces bieten ebenfalls
Einstellungen zur Datenaufbewahrung. Prüfe die geltende Workspace-Konfiguration und die
[Hinweise zu ChatGPT für das Gesundheitswesen](https://help.openai.com/en/articles/20001046-chatgpt-for-healthcare).

Bei der Neuzuweisung eines Projekts oder GPTs werden die privaten
Unterhaltungen oder Dateien des ehemaligen Mitglieds nicht übertragen. Die Person mit Inhaberrechten im Workspace kann diese privaten Inhalte
durch den Wechsel der Inhaberschaft nicht einsehen. Unter
[Entfernung von Workspace-Mitgliedern und Datenaufbewahrung](https://help.openai.com/en/articles/8266418)
findest du Informationen zum aktuellen Verhalten für die einzelnen Tarife.

Wenn Sicherheits- oder Compliance-Anforderungen einen Nachweis der Änderung verlangen, dokumentiere im freigegebenen System
den betroffenen Workspace, die beschäftigte Person, die Zuweisung beim Identitätsanbieter, den Abschlusszeitpunkt,
die für die Genehmigung verantwortliche Person und die Überprüfung des Token-Widerrufs.
Prüfe die verfügbaren Datensätze, Administrationsberechtigungen und Aufbewahrungsregeln in der
[Admin-API-Referenz](https://chatgpt.com/admin/api-reference), für die du angemeldet sein musst.
Für sensible Compliance-Berechtigungsbereiche kann eine Person mit Inhaberrolle im Workspace erforderlich sein. Eine Produktübersicht
findest du unter [Compliance API und Audit-Ereignisse](/de-DE/codex/enterprise/compliance-api).
Leite aus diesem Leitfaden keine Aussagen darüber ab, welche Ereignisse oder Felder erfasst werden oder welche Aufbewahrungsfristen gelten.

## Fehlenden oder unerwarteten Zugriff untersuchen

| Symptom                                               | Was du prüfen solltest                                                                             | Abhilfe                                                                                                       |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Eine beschäftigte Person kann sich anmelden, findet aber den Workspace nicht  | Den Ziel-Workspace, die Einladung, die Zuweisung beim Identitätsanbieter und die E-Mail-Adresse         | Korrigiere die Zuweisung oder die Zuordnung der E-Mail-Adresse und prüfe anschließend die Workspace-Mitgliedschaft                                               |
| Eine über die Synchronisierung verwaltete beschäftigte Person erhält den falschen Platz       | Den Standardplatztyp des Workspace und den aktuellen Mitgliedsdatensatz                     | Lass eine Person mit Inhaberrolle im Workspace den Standardplatztyp und die für die beschäftigte Person unterstützten Platzoptionen prüfen                                     |
| Nach einem Teamwechsel bleibt der Zugriff auf eine Funktion bestehen                | Weitere Gruppenmitgliedschaften, **Direkte Rollen** und die kombinierten Berechtigungen der beschäftigten Person        | Entferne die beschäftigte Person aus nicht mehr benötigten Gruppen. Lass anschließend eine Person mit Inhaberrolle im Workspace ausschließlich die nicht mehr benötigten direkten Rollen dieser Person widerrufen |
| Eine manuell verwaltete Gruppe wird ohne Genehmigung auf SCIM-Verwaltung umgestellt  | Übereinstimmende Gruppennamen, Mitglieder beim Identitätsanbieter, geerbte Rollen und bestehende Freigaben    | Gleiche die Gruppenmitgliedschaft beim Identitätsanbieter mit dem genehmigten Stand ab und prüfe die betroffenen Zugriffsrechte                                 |
| Andere Mitarbeitende verlieren nach einem Teamwechsel den Zugriff       | Kürzliche Änderungen an Rollenzuweisungen für gemeinsam genutzte Gruppen und die genehmigten Zugriffsrechte des bisherigen Teams     | Lass eine Person mit Inhaberrolle im Workspace die genehmigte Rolle der gemeinsam genutzten Gruppe wiederherstellen. Aktualisiere anschließend nur die Mitgliedschaft der Person, die das Team wechselt        |
| Ein für die Automatisierung verwendeter Token funktioniert nach einem Teamwechsel nicht mehr | Die lokale Codex-Berechtigung der für den Ablauf verantwortlichen Person und den aktuellen Token-Status                      | Lass eine Person mit Inhaberrolle im Workspace den genehmigten lokalen Codex-Zugriff wiederherstellen oder ersetze den betroffenen Token durch einen neuen und widerrufe den alten                     |
| Eine Änderung der Zugriffsrechte wird nicht sofort sichtbar           | Den Synchronisierungsstatus des Identitätsanbieters, den erwarteten Synchronisierungszeitraum und kürzliche Rollenänderungen          | Lass die für die Identitätsverwaltung zuständige Person die Synchronisierung prüfen, bevor du den OpenAI-Support kontaktierst                                        |
| Eine entfernte beschäftigte Person wird erneut Mitglied des Workspace           | Die Anwendungszuweisung beim Identitätsanbieter und sämtliche Provisionierungsgruppen, die Zugriff gewähren | Entferne die beschäftigte Person beim Identitätsanbieter statt nur in den Workspace-Einstellungen                                      |
| Für eine ausscheidende beschäftigte Person ist weiterhin ein Token aufgeführt         | Die Person, die den Token erstellt hat, die für den Ablauf verantwortliche Person und die Token-Berechtigungen der Workspace-Administration        | Ersetze alle weiterhin benötigten Automatisierungszugangsdaten und widerrufe anschließend den Token der ausscheidenden beschäftigten Person                                   |
| Eine verbundene Anwendung gewährt weiterhin Zugriff           | Das Konto im Quellsystem, die Verfügbarkeit des Plug-ins und die der Anwendung erteilte Berechtigung                   | Bitte die für den jeweiligen Dienst verantwortliche Person, den Zugriff mit den vom System unterstützten Kontrollen zu entfernen                                  |

Die meisten Identitätsanbieter synchronisieren alle 30 bis 40 Minuten, einige übernehmen Änderungen jedoch sofort. Bis Änderungen an benutzerdefinierten Rollen sichtbar werden, kann es etwa fünf Minuten dauern. Du kannst keine SCIM-Synchronisierung erzwingen. Entferne deshalb kein Workspace-Mitglied, um es anschließend neu anzulegen und so eine verzögerte Aktualisierung zu umgehen.

Wenn der Zugriffsentzug oder die Gruppenaktualisierung nach dem für den jeweiligen Anbieter erwarteten Zeitraum noch nicht abgeschlossen ist, lass die für die Identitätsverwaltung zuständige Person folgende Angaben zusammentragen:

- Den betroffenen Workspace und die E-Mail-Adresse der beschäftigten Person.
- Den Identitätsanbieter, die Anwendungszuweisung und die Provisionierungsgruppe.
- Die versuchte Änderung, ihren Zeitstempel und den neuesten Synchronisierungsstatus.
- Die direkten Rollen, Gruppenrollen oder Token, die noch überprüft werden müssen.

Kontaktiere den [OpenAI-Support](https://help.openai.com/) mit diesen Angaben über
das Hilfecenter. Wenn eine ausgeschiedene beschäftigte Person weiterhin Zugriff hat, behandle dies als sicherheitsrelevanten
Ausnahmefall und befolge den Prozess deiner Organisation zur Eskalation von Vorfällen.

Informationen zum anbieterspezifischen Setup und zum Synchronisierungsverhalten findest du in den aktuellen
[häufigen Fragen zur SCIM-Integration](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq).
Hilfe bei Anmelde- und Identitätsfehlern findest du unter
[Fehlerbehebung bei der Authentifizierung](https://help.openai.com/en/articles/10489721-login-and-authentication-faq-s-and-troubleshooting-sso-scim-and-domain-verification).

## Den gesamten Lebenszyklus von Mitarbeitenden überprüfen

Prüfe vor einem breiteren Rollout alle drei Übergänge mit einer repräsentativen Testperson aus der Belegschaft:

| Lebenszyklusphase | Hauptverantwortung                 | Erfolgreiches Ergebnis                                                                                                            |
| --------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Eintritt          | Für die Identitätsverwaltung zuständige Person        | Die beschäftigte Person wird Mitglied des richtigen Workspace und erhält den vorgesehenen Platz, die vorgesehene Gruppenmitgliedschaft und den vorgesehenen Funktionszugriff                                    |
| Teamwechsel           | Verantwortliche für die Identitätsverwaltung und Personen mit Inhaberrolle im Workspace | Die Administration aktualisiert die Gruppenmitgliedschaft. Personen mit Inhaberrolle im Workspace entfernen nicht mehr benötigte direkte Rollen und behalten die Rollen gemeinsam genutzter Gruppen bei |
| Austritt          | Verantwortliche für Identitätsverwaltung und Sicherheit  | Die Administration entfernt den Workspace-Zugriff, prüft unterstützte Token und widerruft externe Zugriffsrechte oder weist sie neu zu                       |

Dokumentiere, wer die einzelnen Änderungen genehmigt hat, was du überprüft hast und wer dafür verantwortlich ist, verbleibende Ausnahmefälle beim Zugriff zu klären. Plane regelmäßige Zugriffsprüfungen gemäß den Richtlinien deiner Organisation zur Identitätsverwaltung und Sicherheit.

## Weiterführende Dokumentation

- [Leitfaden für den administrativen Rollout](/de-DE/codex/enterprise/admin-setup)
- [Gruppen und Provisionierung](/de-DE/codex/enterprise/groups-and-provisioning)
- [Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions)
- [Kontrollen für Plug-ins](/de-DE/codex/enterprise/apps-and-connectors)
- [Zugriffstoken](/de-DE/codex/enterprise/access-tokens)
- [Dienstkonten](/de-DE/codex/enterprise/service-accounts)
- [Authentifizierung](/de-DE/codex/auth)
- [Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration)
- [Compliance API und Audit-Ereignisse](/de-DE/codex/enterprise/compliance-api)

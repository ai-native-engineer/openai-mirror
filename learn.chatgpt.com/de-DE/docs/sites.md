<!-- source: https://learn.chatgpt.com/de-DE/docs/sites -->

Sites befindet sich in der öffentlichen Beta-Phase und ist in den Tarifen ChatGPT Plus, Pro, Business, Enterprise und Edu verfügbar. Während der Beta-Phase gelten tarifabhängige Nutzungslimits über alle Sites hinweg. ChatGPT zeigt die aktuellen Limits an und benachrichtigt dich, wenn du dich einem Limit näherst. Wenn du ein Limit erreichst, kannst du möglicherweise keine Site erstellen, keinen Speicher hinzufügen oder eine stark genutzte Site öffentlich zugänglich halten. Bestehende Sites kannst du jedoch weiterhin bearbeiten und verwalten.

Mit Sites kann ChatGPT Websites, Web-Apps und Spiele erstellen, hosten, überarbeiten und teilen. Verwende Sites, wenn du auf Grundlage eines Prompts oder eines kompatiblen bestehenden Projekts ein gehostetes Webangebot erstellen möchtest, ohne einen separaten Ablauf für die Bereitstellung einzurichten.

Öffne **Sites** in der ChatGPT-Desktop-App. Du kannst eine Site auf Grundlage eines Prompts oder
eines kompatiblen lokalen Projekts erstellen und anschließend zur Sites-Ansicht zurückkehren, um sie zu verwalten.

Verwende Sites in ChatGPT im Web, um gehostete Sites zu erstellen und zu verwalten. Wähle
**Mehr** \> **Sites** aus oder rufe direkt
[chatgpt.com/sites](https://chatgpt.com/sites) auf, um die von dir erstellten Sites zu finden.

Sites bietet in Codex CLI keine eigenständige Verwaltungsansicht. Verwende ChatGPT im Web oder die Desktop-App, um ein Sites-Projekt zu erstellen, zu speichern, bereitzustellen und zu verwalten. Du kannst Codex CLI weiterhin nutzen, um ein lokales Projekt vor der Veröffentlichung zu bearbeiten und zu testen.

Sites bietet in der IDE-Erweiterung keine eigenständige Verwaltungsansicht. Verwende ChatGPT im Web oder die Desktop-App für Aktionen in Sites und die IDE-Erweiterung, um das lokale Quellprojekt zu bearbeiten und zu testen.

  Jede Bereitstellungs-URL von Sites verweist auf eine Produktivbereitstellung. Wenn du einen Build prüfen möchtest, bevor er online geht, bitte ChatGPT, eine Version zu speichern, ohne sie bereitzustellen.

## Erste Schritte mit Sites

Füge in ChatGPT das Wort „website“ in deinen Prompt ein oder erwähne `@Sites`, um
den Sites-Ablauf gezielt zu starten.

1. Site beschreiben

   Beschreibe die Zielgruppe, den Zweck, das erforderliche Verhalten und die Informationen, die die Site verwenden soll.

2. Site überprüfen

   Überprüfe die generierten Inhalte und das Verhalten. Vergewissere dich, dass die Site die vorgesehenen Informationen verwendet und Daten wie erwartet verarbeitet.

3. Site überarbeiten

   Beschreibe die gewünschten Änderungen. Füge relevante Dateien oder visuellen Kontext hinzu, wenn dies ChatGPT bei der Umsetzung hilft.

4. Site verwalten und teilen

   Kehre zu **Sites** zurück, um die Site erneut zu öffnen oder zu überarbeiten. Wenn sie fertig ist, lege fest, wer
   sie aufrufen darf, und teile den zugehörigen Link.

Wähle in der Vorschau **Bearbeiten** aus. Beschreibe unter **Änderungen an der Website beschreiben** die
gewünschten Änderungen. Verwende **Screenshot** oder **Dateien und mehr hinzufügen** , wenn zusätzlicher
Kontext hilfreich ist.

## Sites per Prompt mit gängigen Aufgaben beauftragen

Gib bei einer neuen Website, einem Dashboard oder einem internen Tool die Zielgruppe, das zentrale Nutzungserlebnis und die erforderlichen Informationen an:

```text
Build a project request dashboard for my operations team. Let team members
submit requests, see who owns each one, update the status, and filter the list.
Require people to sign in with their workspace account, and keep the request
data saved between visits.

Bitte Sites bei einem bestehenden Projekt, die aktuelle App vorzubereiten und zu veröffentlichen:

```text
Deploy this project with Sites. Check whether it is compatible, make any
required changes, and give me the deployment URL.

Wenn eine Site dauerhaft gespeicherte Anwendungsdaten oder hochgeladene Dateien benötigt, gib dies in der Anfrage an:

```text
Add player scores and avatar uploads to this game. Keep the scores and uploaded
avatars between visits.

  Sieh dir die [Anwendungsbeispiele für Sites](/showcase) an. Dort findest du bereitgestellte interne Apps und die vollständigen
  Prompts, mit denen sie erstellt wurden.

## Site-Analysen ansehen

Sites erfasst die Zugriffe automatisch. So kannst du nachvollziehen, wie eine bereitgestellte Site genutzt wird, ohne ein Analyse-SDK hinzuzufügen. Die Analyseansicht zeigt die Gesamtzahl unterschiedlicher Personen, die die Site besucht haben, sowie die Gesamtzahl der Seitenaufrufe. Beide Kennzahlen siehst du auch im zeitlichen Verlauf. Passe den Datumsbereich oder die zeitliche Auflösung an, um einen anderen Zeitraum zu betrachten.

Öffne **Sites**, suche die Site und wähle dann **Weitere Aktionen** \> **Analysen** aus.

Rufe [chatgpt.com/sites](https://chatgpt.com/sites) auf, suche die Site und wähle dann
**Weitere Aktionen** \> **Analysen** aus.

Sites bietet weder in der CLI noch in der IDE-Erweiterung eine eigenständige Analyseansicht. Öffne die Site in ChatGPT im Web oder in der Desktop-App, um ihre Analysen anzusehen.

  

  Analysen sind derzeit für Sites verfügbar, die nicht zu einem Workspace mit ChatGPT Enterprise gehören.

## Anmeldung mit ChatGPT hinzufügen

Öffentliche Sites können für alle zugänglich bleiben und zugleich eine optionale Anmeldung mit ChatGPT für Funktionen anbieten, die die Identität der angemeldeten Person nutzen. Dazu gehören etwa gespeicherte Fortschritte, personalisierte Ansichten oder Datensätze, die einer bestimmten Person gehören. Auf einen Workspace beschränkte Sites verwenden bereits die ChatGPT-Identität, um ihre Freigabeeinstellungen durchzusetzen.

Bitte Sites, die Anmeldefunktion hinzuzufügen:

```text
Add Sign in with ChatGPT to this public Site. Keep the Site available to signed-out visitors. Show a Sign in with ChatGPT action when someone is signed out. After they sign in, greet them with their full name when available, or their email address otherwise. Add a Sign out action, and keep authorization decisions in server-side code.

Sites wickelt die An- und Abmeldung über die von der Plattform bereitgestellten Pfade ab und leitet die Person anschließend zu deiner Site zurück:

```html
<a href="/signin-with-chatgpt">Sign in with ChatGPT</a>
<a href="/signout-with-chatgpt">Sign out</a>

Nach der Anmeldung übermittelt Sites die Identität der Person über die folgenden Request-Header an den Server:

- `oai-authenticated-user-email` enthält die authentifizierte E-Mail-Adresse.
- `oai-authenticated-user-full-name` kann einen nicht leeren Profilnamen enthalten. Behandle
  ihn als optional und verwende ersatzweise die E-Mail-Adresse.

Triff Autorisierungsentscheidungen im serverseitigen Code und verlasse dich nicht auf Header mit getrennten Namensbestandteilen.

## Projekte, Versionen und Bereitstellungen verstehen

Eine Site ist ein dauerhaft gehostetes Webangebot, das du über **Sites** in ChatGPT erneut öffnen, überarbeiten, konfigurieren
und teilen kannst.

Ein Sites-Projekt verknüpft ein lokales Quellprojekt mit dem über Sites verwalteten Hosting.
Sites speichert diese Verknüpfung sowie optionale Namen für Speicherbindungen in
`.openai/hosting.json`. Ein neu erstelltes lokales Starterprojekt kann zunächst ohne
`project_id` auskommen. Sites ergänzt die ID, nachdem es das gehostete Projekt provisioniert hat.

Eine provisionierte Site, die eine Bindung an eine relationale Datenbank, aber keinen Dateispeicher verwendet, kann beispielsweise Folgendes enthalten:

```json
{
  "project_id": "<project-id>",
  "d1": "DB",
  "r2": null
}

Eine Site bleibt auch nach Ende des Chats in ChatGPT Work, in dem sie erstellt wurde, in deiner Sites-Liste sichtbar. Du benötigst weder ein lokales Projekt noch ein Manifest, um eine Site im Web zu starten. Eine Site ist von einem ChatGPT-Projekt getrennt.

Die Veröffentlichung über Sites erfolgt in zwei getrennten Phasen:

1. **Version speichern.** ChatGPT erstellt eine Version, die bereitgestellt werden kann. Bei einem lokalen
   Quellprojekt verknüpft ChatGPT die Version mit dem Git-Commit, der für den
   Build verwendet wurde. Nutze diese Phase, wenn du eine Version vor der Bereitstellung prüfen möchtest.
2. **Version bereitstellen.** ChatGPT veröffentlicht eine gespeicherte Version und zeigt die
   Produktions-URL an, wenn die Bereitstellung erfolgreich ist. Nutze diese Phase nur, wenn
   die ausgewählte Zielgruppe auf die Site zugreifen soll.

Bitte ChatGPT, gespeicherte Versionen aufzulisten oder zu prüfen, wenn du eine frühere Version finden möchtest, die für eine Bereitstellung infrage kommt.

## Unterstützte Site-Architektur auswählen

Bei neuen Projekten kann der Ablauf in Sites mit dem empfohlenen Starterprojekt beginnen. Lass dir bei einem bestehenden Projekt von ChatGPT bestätigen, dass das Projekt kompatible Bereitstellungsartefakte erzeugen kann, bevor du eine Bereitstellung anforderst.

Beschreibe ChatGPT, wie sich das Produkt verhalten soll, damit es die passende Site-Architektur auswählen kann:

| Anforderung an die Site                                                      | Was du bei Sites anfordern solltest                                                         |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Website oder Landingpage mit Schwerpunkt auf Inhalten                            | Eine Site ohne persistenten Anwendungszustand, sofern die gewünschte Funktionalität ihn nicht erfordert |
| Gespeicherte Datensätze, Fortschritte der Nutzenden oder Punktestände in Spielen                   | D1, eine relationale Datenbank für dauerhaft gespeicherte strukturierte Daten                         |
| Bilder, Dokumente, Audio- und Videodateien oder andere Uploads              | R2, Objektspeicher für Dateien                                                  |
| Hochgeladene Dateien mit durchsuchbaren Metadaten                        | D1 für Metadaten und R2 für Dateiinhalte                                      |
| Interne Site, die die Identität der aktuell im Workspace angemeldeten Person benötigt | Identität der über den Workspace authentifizierten Person                                         |
| Öffentliche Anmeldung oder ein externer Identitätsanbieter                | Eine Site mit aktivierter Authentifizierung                                                |

Fordere für vorübergehende Zustände der Benutzeroberfläche wie ein ausgewähltes Design oder ein ausgeblendetes Banner keinen dauerhaften Speicher an. Fordere ihn dagegen für Produktdaten an, bei denen Nutzende erwarten, dass die gehostete Site sie speichert.

## Zugriff und geheime Werte verwalten

Eine neue Site ist nur für die Person, der sie gehört, und Workspace-Administrierende zugänglich, bis du die Zugriffsrechte änderst. Halte den Zugriff beschränkt, während du die Inhalte, den Umgang mit Daten und die vorgesehene Zielgruppe überprüfst.

Je nach deinen Konto- und Workspace-Einstellungen können folgende Freigabeoptionen verfügbar sein:

- **Person, der die Site gehört, und Workspace-Administrierende**
- **Ausgewählte aktive Nutzende oder Gruppen**, sofern unterstützt
- **Eingeladene externe Personen mit Ansichtszugriff**, wenn externe Einladungen verfügbar sind
- **Alle Personen im Workspace**, sofern unterstützt
- **Alle Personen im Internet**, nur wenn die öffentliche Veröffentlichung aktiviert ist

Der Besuchszugriff erlaubt es, die Site zu öffnen, gewährt aber keine Bearbeitungsrechte. In Unternehmens-Workspaces ist die öffentliche Veröffentlichung standardmäßig deaktiviert und muss von einer Person mit Administrationsrechten aktiviert werden.

Bei eingeschränkter Freigabe müssen sich eingeladene Personen mit dem Konto anmelden, dem der Zugriff gewährt wurde. Eine öffentliche Site ist ohne Zugriff auf einen ChatGPT-Workspace verfügbar. Die Zielgruppeneinstellung einer Site und eine gegebenenfalls integrierte Anmeldefunktion werden unabhängig voneinander gesteuert.

Zum Beispiel:

```text
Change this Site's access to everyone in my workspace after showing me the
current Site and confirming its URL.

### Personen außerhalb deines Workspaces einladen

Mit externen Einladungen kannst du bestimmten Personen Zugriff auf eine Site geben, ohne sie öffentlich zu machen. Du kannst Personen außerhalb deines Workspaces zum Ansehen einladen oder eine private Site über ein persönliches Konto teilen. Die Funktion wird schrittweise für Personen verfügbar, die Sites mit einem Plus-, Pro-, Business- oder Enterprise-Abo nutzen.

1. Öffne eine Site, die dir gehört, und wähle **Teilen** aus.
2. Damit die Site privat bleibt, stelle **Wer hat Zugriff** auf **Nur eingeladene Personen** ein.
3. Gib die E-Mail-Adresse der Person unter **Nach Personen oder Gruppen suchen** oder bei einer persönlichen Site unter
**E-Mail-Adresse eingeben** ein. Wähle anschließend die Person aus.
4. Überprüfe die Zielgruppe und die Zugriffsrolle **Kann ansehen** für die eingeladene Person. Wähle dann
**Einladen** aus.
5. Vergewissere dich, dass die Person in der gespeicherten Zugriffsliste erscheint. Teile den Link zur Site und bitte die Person, sich mit dem Konto anzumelden, dem der Zugriff gewährt wurde.

Externe Personen mit Ansichtszugriff können die Site öffnen und nutzen. Sie werden dadurch weder Workspace-Mitglieder noch Bearbeitende der Site und können die Site nicht bearbeiten oder veröffentlichen. Die Einladung gewährt Zugriff auf diese Site. Überprüfe vor dem Teilen ihre Inhalte und die angebundenen Daten.

In Unternehmens-Workspaces verwalten Administrierende die Option **Mitgliedern erlauben, externe Personen zu
Sites einzuladen** unter **Workspace-Einstellungen \> Berechtigungen & Rollen**. Diese Berechtigung
ist unabhängig von der Berechtigung, Sites öffentlich zu veröffentlichen.
Business-Workspaces haben keinen separaten Berechtigungsschalter für externe Einladungen.
Sites muss aktiviert sein und die Funktion muss für das Konto verfügbar sein.
Wenn die Einladungsoption fehlt, überprüfe das ausgewählte Konto, wem die Site gehört,
die Workspace-Berechtigungen und ob die Funktion bereits verfügbar ist.

Um einer Person den Ansichtszugriff zu entziehen, öffne die Freigabeeinstellungen der Site und entferne ihren Zugriff. Überprüfe auch die übrigen Zielgruppeneinstellungen: Das Entfernen einer Einladung entzieht der Person keinen Zugriff, den sie über eine öffentliche Freigabe oder eine Freigabe für den Workspace oder eine Gruppe hat.

### Gemeinsam an einer Site arbeiten

Für die gemeinsame Arbeit an einer Site ist ein Workspace erforderlich. Wenn die Funktion verfügbar ist, kann die Person, der die Site gehört, aktive Mitglieder desselben Workspaces als Bearbeitende einladen.

Bearbeitende können die Live-Daten in der Datenbank der Site einsehen. Lade nur Personen ein, denen du den Code und die Daten der Site anvertraust.

1. Öffne die Site und wähle **Teilen** aus.
2. Suche unter **Personen oder Gruppen hinzufügen** nach einem Workspace-Mitglied und wähle es aus.
   Das Mitglied wird mit Besuchszugriff hinzugefügt.
3. Öffne neben der Person **Kann ansehen** und wähle **Kann bearbeiten** aus. Die Zugriffsrechte werden
   automatisch gespeichert. Die Site erscheint unter **Mit dir geteilt** in der Sites-Ansicht
   des Mitglieds.
4. Die bearbeitungsberechtigte Person kann die Site öffnen, Änderungen vornehmen und Versionen speichern. Updates kann sie veröffentlichen, sobald die Person, der die Site gehört, diese erstmals veröffentlicht hat.

Die Person, der die Site gehört, verwaltet den Bearbeitungszugriff. Sie kann Personen mit bestehendem Besuchszugriff
Bearbeitungsrechte erteilen, Bearbeitende auf **Kann ansehen** zurückstufen oder ihnen den Zugriff entziehen. Für die gemeinsame Bearbeitung kommt
kein separater Schalter für Workspace-Berechtigungen hinzu.

Bearbeitende können die Zielgruppe der Site nicht ändern, keine anderen Personen einladen oder entfernen, keine Einstellungen oder Analysen verwalten, keine frühere Version wiederherstellen und die Inhaberschaft nicht übertragen. Sie können die Site außerdem nicht erstmals veröffentlichen. Das muss zuerst die Person erledigen, der die Site gehört. Erst danach können Bearbeitende weitere Updates veröffentlichen.

Bearbeitungszugriff und Besuchszugriff sind voneinander getrennt. Mit den oben beschriebenen Schritten fügst du die Person zunächst mit Besuchszugriff hinzu und erteilst ihr anschließend Bearbeitungsrechte. Wenn du einer Person mit Besuchszugriff Bearbeitungsrechte erteilst, bleibt die Zielgruppeneinstellung der Site unverändert.

### Werte für die Laufzeitumgebung konfigurieren

Öffne **Sites** und anschließend die Einstellungen der Site, um gehostete
Umgebungsvariablen und geheime Werte hinzuzufügen, zu aktualisieren oder zu entfernen. Nimm geheime Werte nicht in Prompts, angehängte
Dateien oder Site-Inhalte auf.

Rufe [chatgpt.com/sites](https://chatgpt.com/sites) auf, suche die Site und wähle dann
**Weitere Aktionen** \> **Einstellungen** aus.

Speichere diese Werte nicht in `.openai/hosting.json`. Stimme die lokalen Dateien `.env` und
`.env.example` auf die für die lokale Entwicklung benötigten Schlüssel ab und
nimm keine geheimen Werte in Commits auf.

Wenn du gehostete Umgebungswerte hinzufügst, aktualisierst oder entfernst, bitte ChatGPT, die genehmigte gespeicherte Version erneut bereitzustellen, damit die nächste Bereitstellung die aktualisierte Konfiguration verwendet.

## Die URL einer Site ändern

Wenn die URL-Bearbeitung verfügbar ist, kannst du die von ChatGPT gehostete URL einer bestehenden Site ändern, die dir gehört, ohne eine weitere Bereitstellung zu erstellen.

1. Öffne **Sites**, suche die Site und öffne ihre Einstellungen.
2. Suche die URL der Site und wähle **URL ändern** aus.
3. Gib einen verfügbaren Namen ein. Er muss mindestens fünf Zeichen lang sein, mit einem Kleinbuchstaben beginnen und darf nur Kleinbuchstaben, Ziffern und einzelne Bindestriche enthalten. Er darf weder mit einem Bindestrich enden noch mehrere Bindestriche hintereinander enthalten.
4. Bestätige die Änderung und warte, während Sites die Adresse aktualisiert.

Durch die Änderung der URL wird keine weitere Bereitstellung erstellt. Die bisherige Adresse leitet einschließlich aller Routen und Abfrageparameter auf die neue Adresse weiter.

Wenn du die von ChatGPT gehostete URL änderst, wird keine benutzerdefinierte Domain hinzugefügt, entfernt oder geändert. Benutzerdefinierte Domains sind eine eigenständige, bereits bestehende Funktion. Nutze die Einstellungen für benutzerdefinierte Domains, sofern die Funktion verfügbar ist.

## Eine benutzerdefinierte Domain verbinden

Wenn benutzerdefinierte Domains verfügbar sind, kannst du eine Apex-Domain oder Subdomain verbinden, die dir bereits gehört. Sites registriert keine Domains für dich. Du musst daher die DNS-Einträge der Domain ändern können. Zum Start sind benutzerdefinierte Domains in Unternehmens-Workspaces nicht verfügbar.

So verbindest du eine Domain:

1. Öffne die Einstellungen der Site und wähle **Domain hinzufügen** aus.
2. Gib die Apex-Domain oder Subdomain ein, die du verwenden möchtest.
3. Kopiere die von Sites bereitgestellten DNS-Einträge und die zugehörigen Werte und trage sie bei deinem Domainanbieter ein.
4. Warte einige Minuten. Kehre dann zu den Einstellungen der Site zurück und aktualisiere den Domainstatus.

Du kannst ChatGPT auch bitten, dir bei der Verknüpfung der Domain mit deiner Site zu helfen. Wenn die Browsernutzung oder die Computernutzung aktiviert ist, kann ChatGPT dich nach deiner Anmeldung durch die Oberfläche deines Domainanbieters führen.

## Vor der Freigabe überprüfen

Bevor du eine Site freigibst:

- Überprüfe ihre Inhalte, generierten Texte und Bilder, Links, hochgeladenen Dateien und Formulare sowie ihr Verhalten bei Interaktionen.
- Vergewissere dich, dass sie keine vertraulichen oder sensiblen Informationen, geheimen Werte oder Inhalte Dritter offenlegt, die du nicht weitergeben darfst.
- Teste die Site aus Sicht der vorgesehenen Besuchenden und prüfe dabei auch den Zugriff und die Anmeldung.
- Überprüfe Funktionen, die personenbezogene Informationen oder andere Inhalte von Besuchenden erfassen. Entscheide, ob die Site diese Informationen erfassen, weitergeben oder veröffentlichen soll.
- Wenn die Site die Anmeldung mit ChatGPT nutzt, erkläre, welche Informationen über Besuchende sie erhält und wie sie diese verwendet.
- Wenn die Site personenbezogene Daten erfasst oder verarbeitet, halte dich an
[die geltenden Gesetze zum Schutz der Privatsphäre und zum Datenschutz](https://help.openai.com/en/articles/20001340).
- Wähle die restriktivste Freigabeoption, die zur vorgesehenen Zielgruppe passt.
- Öffne die freigegebene Site und prüfe, ob die vorgesehene Zielgruppe darauf zugreifen kann.

Wenn die Site aus einem lokalen Projekt erstellt wurde, überprüfe auch die Änderungen am Quellcode und etwaige
Datenbankmigrationen im [Review-Bereich](/de-DE/codex/code-review?surface=app) von Codex.

## Zugriff auf eine Site entziehen oder die Site löschen

Um den Zugriff zu entziehen, ohne die Site zu löschen, öffne ihre Freigabeeinstellungen und beschränke den Zugriff auf dich selbst oder ausgewählte Personen. Prüfe, ob die bisherige Zielgruppe die Site nicht mehr öffnen kann.

So löschst du eine Site dauerhaft:

1. Öffne **Sites** und suche die Site.
2. Wähle **Site löschen** und folge den angezeigten Anweisungen.
3. Gib den Slug der Site ein und wähle dann **Dauerhaft löschen**.

Wenn du eine Site löschst, wird sie dauerhaft entfernt. Eine gelöschte Site kannst du nicht wiederherstellen.

## Limits und nicht unterstützte Anwendungsfälle verstehen

Sites hostet Webangebote, die in der unterstützten Sites-Laufzeitumgebung ausgeführt werden. Einige Frameworks, private Netzwerke, Datenbanken, Hintergrunddienste und Hosting-Modelle werden nicht unterstützt.

HTTP, HTTPS und WebSockets werden unterstützt. Direkte eingehende und ausgehende TCP-Verbindungen werden nicht unterstützt.

Für jede Site gelten folgende Speicherlimits:

| Ressource            | Limit                  |
| ------------------- | ---------------------- |
| D1-Datenbankspeicher | 10 GB                  |
| R2-Objektspeicher   | Kein festes Speicherlimit |

Zum Start unterstützt Sites weder Datenresidenz noch Inferenzresidenz. Das gilt für bereitgestellte Sites, den Site-Code, in D1 und R2 gespeicherte Daten und Dateien, generierte Artefakte sowie Protokolle.

Verwende Sites nicht, um geschützte Gesundheitsinformationen oder Zahlungskartendaten zu verarbeiten;
Kinder unter 13 Jahren oder unter dem jeweils geltenden Mindestalter für die digitale Einwilligung anzusprechen;
Finanztransaktionen zu ermöglichen; Malware zu verbreiten; Phishing zu ermöglichen; dich als andere Personen
oder Organisationen auszugeben oder anderweitig gegen die Richtlinien von OpenAI zu verstoßen. Unter
[ChatGPT Sites erstellen und verwalten](https://help.openai.com/en/articles/20001339)
findest du die aktuellen Limits und Links zu den Richtlinien.

## Weiterführende Dokumentation

- [ChatGPT-Desktop-App](/de-DE/codex/app) stellt die Navigation in der App sowie Projekte und Chats vor.
- [Änderungen überprüfen und veröffentlichen](/de-DE/codex/code-review?surface=app) erklärt, wie du Änderungen am Quellcode
  vor der Veröffentlichung überprüfst.

- [Projekte und Chats](/de-DE/codex/projects) erklärt, wie der Kontext von Ordnern und Workspaces
  über mehrere Chats hinweg erhalten bleibt.
- [Änderungen überprüfen und veröffentlichen](/de-DE/codex/code-review) erläutert den Review-Ablauf für
  jeden Codex-Client.
- [Sandboxing](/de-DE/codex/sandboxing) erklärt die Grenzen der lokalen Ausführung.

- [Öffne Sites in ChatGPT](https://chatgpt.com/sites), um zu den von dir erstellten Sites
  zurückzukehren.
- [Projekte und Chats](/de-DE/codex/projects?surface=web) erklärt, wie du zusammengehörige Chats
  und Quelldateien gemeinsam verwaltest.
- [Mit Dateien arbeiten](/de-DE/codex/artifacts-viewer?surface=web) erklärt, wie du generierte Dateien
  in ChatGPT im Web überprüfst.

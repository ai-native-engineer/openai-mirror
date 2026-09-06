<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/apps-and-connectors -->

Plug-ins bündeln wiederverwendbare Arbeitsabläufe und können Skills sowie Apps enthalten,
die Verbindungen zu anderen Tools herstellen. Auf unterstützten Oberflächen verwenden
ChatGPT und Codex dasselbe öffentliche Plug-in-Verzeichnis. Administrierende entscheiden,
welche Plug-ins in ihrem Workspace verfügbar sind. Erfahre mehr über [Plug-ins](/de-DE/codex/plugins),
[Skills](/de-DE/codex/skills-and-plugins) und
[Apps und Konnektoren](https://help.openai.com/en/articles/11487775).

Ein Mitglied kann eine konnektorgestützte Funktion nur nutzen, wenn das Plug-in und die App
für seine Rolle verfügbar sind und es Zugriff auf den verbundenen Dienst hat.

Plug-ins lassen sich in Chat und Work in ChatGPT im Web, auf dem Desktop und auf Mobilgeräten nutzen,
außerdem in Codex in der ChatGPT-Desktop-App sowie über den Plug-in-Browser der Codex CLI.
In der IDE-Erweiterung sind sie nicht verfügbar.

Wie diese Kontrollen mit Rollen und Berechtigungen im Workspace zusammenhängen, erfährst du unter
[Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions).

## Zusammenspiel der Funktionsebenen verstehen

Ein Plug-in kann folgende Steuerungsebenen umfassen:

| Ebene                   | Was sie festlegt                                                           | Wo sie verwaltet wird                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Verfügbarkeit            | Ob das Plug-in-Paket der jeweiligen Person zur Verfügung steht                           | [Workspace-Einstellungen](https://chatgpt.com/admin/settings) für unterstützte Web- und Desktop-Oberflächen; der CLI-Plug-in-Browser für die CLI |
| Enthaltene Skills         | Welche wiederverwendbaren Anweisungen das installierte Plug-in bereitstellt                 | Das Plug-in-Paket und die [Kontrollen für Skills](/de-DE/codex/enterprise/skills)                                                               |
| App-Zugriff              | Ob Nutzende eine konnektorgestützte Funktion verwenden können                          | [Workspace-Apps](https://chatgpt.com/admin/ca) und [Berechtigungen und Rollen](https://chatgpt.com/admin/settings)                    |
| Aktionen und Berechtigungen | Welche Aktionen Nutzende ausführen können und wann ChatGPT vor der Verwendung des Konnektors nachfragt | Die Aktionssteuerung des Konnektors und die App-Berechtigungen unter [Workspace-Apps](https://chatgpt.com/admin/ca)                            |
| Autorisierung beim Dienst   | Auf welche externen Daten und Aktionen die authentifizierte Identität zugreifen kann        | Der verbundene Dienst und sein Identitätsanbieter                                                                                 |
| Laufzeitberechtigungen     | Was ein Agent tun kann, nachdem er Daten oder ein Tool erhalten hat                        | Die Steuerung von Laufzeit, Sandbox und Genehmigungen für die aktive Oberfläche                                                              |

Führe den Rollout über diese Ebenen in zwei Schritten durch: Stelle zuerst die passenden Plug-ins bereit
und konfiguriere anschließend die Funktionen und Berechtigungen, die für den jeweiligen Ablauf erforderlich sind.

## Schritt 1: Plug-ins verfügbar machen

Auf unterstützten Web- und Desktop-Oberflächen legen die Kontrollen für Plug-ins im Workspace fest,
welche Rollen ein Plug-in nutzen oder installieren können. Die Codex CLI verwendet
für die Installation ihren eigenen Plug-in-Browser. Die Anleitung
[Plug-ins erstellen](https://developers.openai.com/plugins/build/plugins) beschreibt die
Paketierung und Verteilung.

Wie du Plug-ins für deinen Workspace aus GitHub importierst und aktuell hältst, erfährst du unter
[Plug-in-Verwaltung](/de-DE/codex/enterprise/plugin-management).

### Öffentlichen Katalog zur Überprüfung exportieren

Berechtigte Personen mit Inhaber- oder Administrationsrechten in einem ChatGPT Enterprise-Workspace können eine CSV-Datei
mit den öffentlichen Plug-ins herunterladen, die für ihren Workspace verfügbar sind. Nutze den Export, um die Metadaten
von Plug-ins, Apps und Skills zu überprüfen, bevor du die Verfügbarkeit von Plug-ins änderst.

1. Öffne [Admin \> Plug-ins](https://chatgpt.com/admin/plugins).
2. Wähle **Öffentlich** aus.
3. Wähle in der Kopfzeile der Seite das Download-Symbol (**CSV exportieren**) aus.

Die heruntergeladene Datei heißt `public-plugins-security-review.csv` und enthält:

- Plug-in-Metadaten: `Plugin Name`, `Plugin Description`, `Date Added (UTC)`,
`OpenAI Verified`, `Developer Name` und `Version`.
- App-Metadaten: `App Name(s)` und `App Description(s)`.
- Metadaten zu Chat-Skills: `Skill Name(s)` und `Skill Description(s)`.

Enthält ein Plug-in mehrere Apps oder Skills, sind die entsprechenden Werte durch Semikolons getrennt.
Der Export basiert auf einer Momentaufnahme des öffentlichen Katalogs, die bis zu 48 Stunden alt sein kann.
Er enthält ausschließlich öffentliche Plug-ins, die für den aktuellen Workspace sichtbar sind, jedoch keine
für diesen Workspace erstellten Plug-ins. In FedRAMP-Workspaces ist der Export nicht verfügbar.

## Schritt 2: Funktionen verwalten

  Die Bereitstellung einer App oder eines Plug-ins in ChatGPT gewährt keinen Zugriff auf Dateien,
Datensätze oder Aktionen im verbundenen Dienst. Bevor du Fehler behebst oder den Zugriff erweiterst,
prüfe die Rolle des Mitglieds im Workspace und die genehmigten Aktionseinstellungen. Stelle anschließend sicher,
dass das authentifizierte Konto oder die gemeinsam genutzte Verbindung über die erwarteten Berechtigungen
im verbundenen Dienst verfügt.

Plug-ins in ChatGPT und Codex können Konnektoren enthalten, die externe Systeme durchsuchen,
Daten abrufen, Daten synchronisieren oder Aktionen in diesen Systemen ausführen. Die Verfügbarkeit von
Plug-ins sowie die gewährten Zugriffsrechte und erlaubten Aktionen für jeden Konnektor werden getrennt gesteuert.

Verwalte konnektorgestützte Funktionen über
[Workspace-Apps](https://chatgpt.com/admin/ca) und
[Berechtigungen und Rollen](https://chatgpt.com/admin/settings). Mit den verfügbaren Kontrollen
können Administrierende:

- Apps oder Konnektoren aktivieren und den Zugriff anhand der Workspace-Rolle vergeben.
- Bei Konnektoren mit Aktionssteuerung Aktionen ohne Schreibzugriff oder eine genehmigte
benutzerdefinierte Auswahl zulassen und festlegen, wie der Workspace mit neu hinzugefügten Aktionen umgeht.
- App-Berechtigungen festlegen, die bestimmen, wann ChatGPT vor der Nutzung einer App nachfragt.
- Den Zugriff auf die Berechtigungsbereiche und Berechtigungen beschränken, die der jeweilige verbundene
Dienst und die authentifizierte Person gewähren.

Aktuelle Informationen zu Verfügbarkeit und Vorgehensweisen findest du unter
[Administrative Steuerung, Sicherheit und Compliance in Apps](https://help.openai.com/en/articles/11509118).

<a id="choose-a-starting-set-of-apps"></a>

## Eine gezielte Erstauswahl treffen

Beginne mit Plug-ins, die einen konkreten geschäftlichen Bedarf abdecken. Entscheide für jedes Plug-in,
ob es allen zur Verfügung stehen, auf eine Rolle oder Pilotgruppe beschränkt werden oder zunächst
weiter geprüft werden soll.

Dokumentiere für jeden verbundenen Dienst die fachlich verantwortliche Person, die zulässigen Daten,
die genehmigten Lese- oder Schreibaktionen, die Authentifizierungsmethode sowie eine Ansprechperson
für Support oder die Entfernung des Dienstes.

Bevor du Schreibaktionen aktivierst oder eine neue angebundene Funktion veröffentlichst, überprüfe,
für welche Rollen sie freigegeben ist. Teste sie mit einem Konto, das im verbundenen Dienst
nur über die vorgesehenen Berechtigungen verfügt.

Beginne bei einem umfassenden Rollout mit Kategorien, die Teams täglich verwenden, etwa E-Mail,
Kalender sowie Datei- oder Dokumentensystemen. Prüfe im
[Plug-in-Verzeichnis](https://chatgpt.com/apps) die aktuelle Verfügbarkeit
und die Funktionen auf den unterstützten Oberflächen von ChatGPT und Codex.

Beginne unabhängig von der ersten Auswahl mit Leseaktionen. Bevor du Schreibaktionen aktivierst,
ermittle die für das Plug-in verantwortliche Person, prüfe die Berechtigungsbereiche des Konnektors und
die Berechtigungen im Dienst, überprüfe den Datenzugriff und dokumentiere externe Auswirkungen sowie eine
Möglichkeit zur Wiederherstellung.

## Datenfluss und Sicherheit verstehen

Wenn ChatGPT eine App oder einen Konnektor aus einem Plug-in verwendet, sendet es eine Anfrage
an den verbundenen Dienst und gibt Daten oder Aktionsergebnisse zurück, die gemäß den Berechtigungen
der authentifizierten Person in diesem Dienst zulässig sind.

ChatGPT verarbeitet Daten aus verbundenen Apps auf zwei Arten:

- **Nicht synchronisiert:** ChatGPT verarbeitet Daten aus Chat und Deep Research nur vorübergehend
  und indexiert sie nicht.
- **Synchronisiert:** ChatGPT indexiert ausgewählte Inhalte aus verbundenen Diensten im Voraus. Auf der Plug-in-Seite
  kannst du sehen, ob eine App die Synchronisierung unterstützt.

Der jeweilige Modus bestimmt, wie ChatGPT Inhalte aus verbundenen Diensten indexiert. Er ersetzt nicht die
üblichen Einstellungen zur Aufbewahrung von Chats. ChatGPT-Unterhaltungen, in denen Apps verwendet werden,
bleiben über die Compliance API verfügbar.

Die App-Dokumentation von OpenAI beschreibt die Verschlüsselung bei der Übertragung und im Ruhezustand, die Autorisierung pro Person, Rollen- und Aktionskontrollen sowie den eingeschränkten Netzwerkzugriff für Unterhaltungen, in denen Apps verwendet werden. Sie hält außerdem fest, dass bei Business, Enterprise und Edu keine über Apps abgerufenen Informationen zum Modelltraining verwendet werden. Wenn eine Anfrage einen verbundenen Dienst erreicht, gelten auch dessen Berechtigungsbereiche, Aufbewahrungsregeln, Vorgaben zur Datenresidenz und weitere Richtlinien.

Unter [App-Sicherheit und Compliance](https://help.openai.com/en/articles/11509118)
und [Apps mit Synchronisierung](https://help.openai.com/en/articles/10847137) findest du aktuelle Informationen zum
Umgang mit Daten. Informationen zu lokal konfigurierten MCP-Servern in der ChatGPT-Desktop-App,
der Codex CLI oder der IDE-Erweiterung findest du unter
[MCP-Konfiguration für Codex](/de-DE/codex/extend/mcp).

## Aktuelle Anleitungen und Referenzen nutzen

- [Administrationsfunktionen, Sicherheit und Compliance in Apps](https://help.openai.com/en/articles/11509118)
- [Apps in ChatGPT](https://help.openai.com/en/articles/11487775)
- [Apps mit Synchronisierung](https://help.openai.com/en/articles/10847137)
- [Workspace-Einstellungen verwalten](https://help.openai.com/en/articles/8411955)
- [Plug-ins](/de-DE/codex/plugins)
- [Skills und Plug-ins](/de-DE/codex/skills-and-plugins)
- [Plug-ins erstellen](https://developers.openai.com/plugins/build/plugins)
- [Leitfaden für den administrativen Rollout](/de-DE/codex/enterprise/admin-setup)

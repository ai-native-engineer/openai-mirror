<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/admin-setup -->

Nutze diesen Leitfaden, um einen Rollout von ChatGPT Enterprise für folgende Verwaltungsbereiche zu planen:

- Workspace-Zugriff.
- Lokale Laufzeitrichtlinie für die betreffenden Funktionen in der ChatGPT-Desktop-App, der Codex CLI und der IDE-Erweiterung.
- Codex Cloud.
- Zugriff auf die Platform API.
- Zugriff auf Plug-ins und Konnektoren.
- Berechtigungen in verbundenen Systemen.

Führe die Schritte bei einem neuen Rollout der Reihe nach aus oder nutze die verlinkten Seiten, um einen einzelnen Bereich zu ändern.

In den Workspace-Einstellungen fasst **Codex und Work lokal** den lokalen Zugriff auf Codex und Work
unter **Mitgliedern erlauben, Codex und Work lokal zu nutzen** zusammen. Einige Workspaces
haben stattdessen separate Bereiche für **Codex lokal** und **Work lokal** . In
dieser Ansicht steuert **Mitgliedern erlauben, Codex lokal zu nutzen** den Zugriff auf Codex und **Work
lokal nutzen** den Zugriff auf Work. Wenn du eine der beiden Optionen aktivierst, wird die andere dadurch nicht aktiviert.
Diese Bezeichnungen stehen für Workspace-Berechtigungen, nicht für separate Produkte oder Clients.
Token-Berechtigungen und Beschränkungen der Gültigkeitsdauer von Zugangsdaten findest du je nach Workspace entweder im Bereich **Token für den
Zugriff** oder im Bereich für den lokalen Zugriff.
Die verwaltete Konfiguration bildet eine separate Richtlinienebene, die das unterstützte
Laufzeitverhalten der betreffenden Funktionen in diesen Clients einschränken kann. Dieser Leitfaden nennt
die jeweilige Oberfläche, wenn sich Verhalten oder Verfügbarkeit unterscheiden.

Beginne mit der maßgeblichen Übersicht unter
[Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions).
Nutze für aktuelle Verfahren im ChatGPT-Workspace die Anleitungen im Hilfecenter und für das
lokale sowie gehostete Laufzeitverhalten die verlinkte Dokumentation für die Entwicklung.

<a id="enterprise-grade-security-and-privacy"></a>

Informationen zu Sicherheit, Datenschutz und Laufzeitschutz für Unternehmen findest du unter
[Genehmigungen und Sicherheit für Agenten](/de-DE/codex/agent-approvals-security) sowie im
[Whitepaper zur Sicherheit von Codex](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click).

<a id="pre-requisites-determine-owners-and-rollout-strategy"></a>

## Schritt 1: Verantwortliche und Art des Rollouts festlegen

Lege für jeden Teil des Rollouts eine verantwortliche Person fest:

- **Workspace-Zugriff:** Mitgliedschaft, Lizenzen, Rollen und
  unterstützte Workspace-Funktionen.
- **Lokale Laufzeitrichtlinie:** Genehmigungen, Berechtigungsprofile, Dateisystem- und
  Netzwerkzugriff sowie weitere Anforderungen für unterstützte lokale Clients.
- **Codex Cloud:** Gehostete Umgebungen, Repository-Verbindungen und
  Laufzeitrichtlinie für die Cloud.
- **Verbundene Systeme:** Installation von Anwendungen beim Anbieter, Konten und
  Berechtigungen.
- **Berichterstellung und Compliance:** Zugriff auf Analysen, Exporte von Audit-Daten und
  nachgelagerte Datenverarbeitung.

Entscheide für jede Zielgruppe, ob sie die betreffenden lokalen Funktionen der ChatGPT-Desktop-App, der Codex CLI oder der IDE-Erweiterung, Codex Cloud oder eine Kombination davon benötigt. Behandle den Zugriff auf die Platform API als separaten Zugriffsbereich auf Organisations- und Projektebene, wenn ein Arbeitsablauf die Authentifizierung per API-Schlüssel nutzt.

## Schritt 2: Workspace-Zugriff und Identität konfigurieren

Nutze Mitgliedschaften, Lizenzen und Gruppen im ChatGPT-Workspace sowie unterstützte RBAC-Berechtigungen, um den vorgesehenen Zielgruppen Zugriff auf unterstützte Workspace-Funktionen zu gewähren. Prüfe den Zugriff auf lokale Clients und Codex Cloud anhand der aktuellen Workspace-Dokumentation, statt davon auszugehen, dass dieselbe Rolle den Zugriff auf jede Oberfläche regelt. Vergib integrierte Administrationsrollen nur an Personen, die den Workspace verwalten.

Die Steuerelemente und Bezeichnungen im Workspace ändern sich mit der Zeit. Aktuelle Verfahren findest du in diesen Quellen:

- [Mitglieder, Lizenztypen, Rollen und Zugriff verwalten](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [Rollenbasierte Zugriffskontrolle konfigurieren](https://help.openai.com/en/articles/11750701-rbac)
- [Workspace-Einstellungen verwalten](https://help.openai.com/en/articles/8411955)
- [Gruppen und Provisionierung](/de-DE/codex/enterprise/groups-and-provisioning)
- [Verwaltung des Lebenszyklus von Nutzerkonten](/de-DE/codex/enterprise/user-lifecycle)
- [Authentifizierung](/de-DE/codex/auth)

Teste die Anmeldung und den Funktionszugriff mit einem repräsentativen Mitglied, bevor du den Rollout ausweitest. Der Workspace-Zugriff gewährt keinen Zugriff auf Repositorys, Dateien oder Aktionen in einem verbundenen Dienst.

## Schritt 3: Lokale Laufzeitanforderungen konfigurieren

Lokale Anforderungen schränken das Laufzeitverhalten ein, wenn jemand eine unterstützte
lokale Ausführung in der ChatGPT-Desktop-App, der Codex CLI oder der IDE-Erweiterung startet. Stelle
`requirements.toml` über einen unterstützten Cloud-, Geräte- oder Systemkanal bereit. Halte
diese Richtlinie von Rollen und Gruppen im ChatGPT-Workspace getrennt.

Verwende für unterstützte lokale Clients Berechtigungsprofile, statt bei neuen Bereitstellungen auf die bisherigen Einschränkungen des Sandbox-Modus zu setzen. Beispiel:

```toml
default_permissions = ":workspace"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true

Um die Computernutzung auf allen unterstützten Browser- und Desktop-Oberflächen zu deaktivieren, schränke jeden öffentlichen Funktionsschlüssel ein, der an der Computernutzung beteiligt ist:

```toml
[features]
browser_use = false
browser_use_full_cdp_access = false
browser_use_external = false
in_app_browser = false
computer_use = false

Die maßgebliche Schlüsselliste, Angaben zu Bereitstellungsverhalten und Vorrangregeln sowie weitere
Beispiele findest du unter
[Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration) und in der
[Referenz zu `requirements.toml`](/de-DE/codex/config-file/config-reference#requirementstoml).

<a id="team-config"></a>
<a id="step-4-standardize-local-configuration-with-team-config"></a>

## Schritt 4: Repository-Konfiguration standardisieren

Nutze eine Konfiguration auf Repository-Ebene, um Standardwerte für das Projekt, Regeln und
Skills gemeinsam bereitzustellen, ohne das Setup für jede Person zu wiederholen. Checke die Konfiguration je nach dokumentiertem Speicherort der jeweiligen Funktion unter
`.codex` oder `.agents` ein:

| Typ          | Quelle                                           | Verwendungszweck                                                  |
| ------------- | ------------------------------------------------ | ---------------------------------------------------------- |
| Konfiguration | [Grundlagen der Konfiguration](/de-DE/codex/config-file/config-basic) | Standardwerte für unterstützte lokale Clients auf Repository-Ebene festlegen        |
| Regeln         | [Regeln](/de-DE/codex/agent-configuration/rules)        | Befehle steuern, die außerhalb der Sandbox eine Genehmigung erfordern |
| Skills        | [Skills erstellen](/de-DE/codex/build-skills)              | Arbeitsabläufe im Repository für unterstützte Clients verfügbar machen   |

Die Repository-Konfiguration kann Standardwerte und wiederverwendbare Arbeitsabläufe bereitstellen. Sie kann keinen Zugriff auf den Workspace, Modelle, die Platform API oder verbundene Systeme gewähren.

## Schritt 5: Codex Cloud konfigurieren

Codex Cloud nutzt gehostete Umgebungen und verbundene Quellcode-Repositorys. Plane jeden Bereich separat:

1. Gewähre der vorgesehenen Zielgruppe über unterstützte Workspace-Steuerelemente Zugriff auf Codex Cloud.
2. Installiere und konfiguriere die unterstützte Integration des Quellsystems.
3. Beschränke den Repository-Zugriff im Quellsystem auf die Repositorys, die die jeweilige Zielgruppe benötigt.
4. Konfiguriere Cloud-Umgebungen, Secrets und Internetzugang für diese Repositorys.
5. Konfiguriere optionale gehostete Arbeitsabläufe wie Code Review.
6. Teste mit einer repräsentativen Person, die über die vorgesehenen Workspace- und Repository-Berechtigungen verfügt.

Codex Cloud hält die Repository-Berechtigungen und Schutzmechanismen ein, die das
verbundene Quellsystem bereitstellt. Der Workspace-Zugriff setzt diese Kontrollen nicht außer Kraft. Unter
[Cloud-Umgebungen](/de-DE/codex/environments/cloud-environment),
[GitHub-Integration](/de-DE/codex/third-party/github) und
[Genehmigungen und Sicherheit für Agenten](/de-DE/codex/agent-approvals-security) findest du Hinweise zum Setup und zum
Laufzeitverhalten von Codex Cloud.

## Schritt 6: Plug-ins und verbundene Funktionen konfigurieren

Prüfe die Installation von Plug-ins, mitgelieferte Skills, konnektorgestützte Funktionen, Konnektoraktionen und die Autorisierung im Quellsystem und entscheide über jeden dieser Punkte separat. Das Deaktivieren einer konnektorgestützten Funktion führt nicht zwangsläufig dazu, dass das Plug-in oder die mitgelieferten Skills deinstalliert werden.

Bevor du ein Plug-in oder einen Skill in den Rollout aufnimmst:

1. Prüfe die Quelle, die verantwortliche Person, die vorgesehene Zielgruppe und das Datum der Überprüfung.
2. Überprüfe die mitgelieferten Skills, Konnektoren, MCP-Server und Hooks sowie die Daten und Aktionen, die jede Funktion erfordert.
3. Führe den Test mit nicht sensiblen Daten und den minimal erforderlichen Zugriffsrechten durch.
4. Dokumentiere, wer für die erneute Überprüfung und die Außerbetriebnahme verantwortlich ist.

Plug-ins funktionieren in Chat und Work in ChatGPT im Web, auf dem Desktop und auf Mobilgeräten, in Codex in der ChatGPT-Desktop-App sowie über den Plug-in-Browser der Codex CLI. In der IDE-Erweiterung sind sie nicht verfügbar. ChatGPT und Codex nutzen ein gemeinsames universelles öffentliches Plug-in-Verzeichnis. Die Zugriffssteuerungen des Workspace bestimmen, auf welche dieser Plug-ins Mitglieder zugreifen können.

Das vollständige Modell findest du unter [Kontrollen für Plug-ins](/de-DE/codex/enterprise/apps-and-connectors) und
[Kontrollen für Skills](/de-DE/codex/enterprise/skills).

## Schritt 7: Governance und Beobachtbarkeit einrichten

Wähle je nach Fragestellung die passende Berichtsoberfläche aus:

<a id="analytics-api-setup-steps"></a>
<a id="compliance-api-setup-steps"></a>

- Nutze [Workspace-Analysen](/de-DE/codex/enterprise/workspace-analytics) für
  interaktive Analysen für den ChatGPT-Workspace und für Codex.
- Nutze die [Analyse-API](/de-DE/codex/enterprise/analytics-api) für programmatisch erstellte,
  aggregierte Berichte über die Analyse-API von Codex.
- Nutze die [Compliance API](/de-DE/codex/enterprise/compliance-api) für Audit- und
  Untersuchungsdatensätze.
- Nutze [ChatGPT-Nutzungslimits und Ausgabenkontrollen](/de-DE/codex/enterprise/usage-limits),
  wenn Codex-Aktivitäten je nach Tarif dafür vorgesehene
  Credits des ChatGPT-Workspace verbrauchen.

Nutze die nur nach Authentifizierung zugänglichen API-Referenzen für aktuelle Angaben zu Zugriffsanforderungen, Schemas, Feldern, Datenaufbewahrung und dem Verhalten bei Anfragen. Entwickle keine Integration anhand einer in diesen Leitfaden kopierten Schnittstellendefinition.

Sichere die Integrationsgrenze ab:

- Speichere API-Schlüssel und andere Zugangsdaten für Integrationen im Secret-Management-System der Organisation.
- Beschränke den Zugriff auf nachgelagerte Systeme und aufbewahrte Daten auf den autorisierten Personenkreis.
- Schütze exportierte Datensätze der Compliance API entsprechend ihrer Sensibilität und der Aufbewahrungsrichtlinie der Organisation. Teste die Arbeitsabläufe zur Erfassung und Löschung anhand der aktuellen Schnittstellendefinition.

## Schritt 8: Rollout überprüfen und aktuell halten

Überprüfe alle relevanten Bereiche mit repräsentativen Identitäten:

- Mitgliedschaft, Lizenzplatz und unterstützte Rollenberechtigungen im ChatGPT-Workspace.
- Einbezogene lokale Funktionen in der ChatGPT-Desktop-App, der Codex CLI und der IDE-Erweiterung, einschließlich Anmeldung und tatsächlich geltender Laufzeitanforderungen.
- Zugriff auf Codex Cloud, Konfiguration der Umgebung und Repository-Berechtigungen.
- Organisations- und Projektzugriff in der Platform API für Arbeitsabläufe mit API-Schlüsseln.
- Installation von Plug-ins, mitgelieferte Skills, Zugriff auf Konnektoren und unterstützte Aktionen.
- Autorisierung und Datenzugriff in verbundenen Systemen.
- Zugriff auf Analyse- und Compliance-Funktionen für die zuständigen Administrierenden.

Dokumentiere für jede Kontrollmaßnahme die zuständige Stelle und die maßgebliche Quelle für das jeweils aktuelle Verfahren. So können Administrierende bei Änderungen an der Benutzeroberfläche oder an Richtlinien die Verfahren aktualisieren, ohne das Administrationsmodell zu ändern.

Überprüfe nach dem ersten Rollout die Zugriffsrechte, die verbundenen Funktionen, die Nutzung von Credits, die Rückmeldungen aus dem Support und die von den Teams tatsächlich genutzten Arbeitsabläufe. Passe den Umfang des Rollouts und die Leitlinien für Administrierende an, wenn sich diese Faktoren ändern.

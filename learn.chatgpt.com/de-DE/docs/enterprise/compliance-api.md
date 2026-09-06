<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/compliance-api -->

Verwende die Compliance API für Arbeitsabläufe in den Bereichen Sicherheit, Recht, Governance und Untersuchungen,
für die prüfbare Aufzeichnungen erforderlich sind. Nutze Analysen statt Compliance-Datensätzen,
um Nutzung und Trends zu messen.

Die [Admin-API-Referenz](https://chatgpt.com/public/admin/api-reference)
ist die maßgebliche Quelle für aktuelle Zugriffsanforderungen, abgedeckte Ereignisse, Routen,
Schemas, Filter, Aufbewahrung und das Verhalten bei Anfragen.

Eine Übersicht über die verfügbaren Compliance-Funktionen und gängigen
Integrationsmuster findest du im [Leitfaden zur Compliance-Plattform](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).

## Wann du die Compliance API verwenden solltest

Die Compliance API eignet sich, wenn du Folgendes tun musst:

- Unterstützte Datensätze in ein Audit- oder Untersuchungssystem exportieren.
- Aufbewahrungs- und Legal-Hold-Prozesse deiner Organisation anwenden.
- Codex-Aktivitäten mit anderen Sicherheits- oder Identitätsdaten korrelieren.
- Genehmigte Untersuchungen zu Sicherheits-, Rechts- oder Governance-Fragen unterstützen.

Die Compliance API ist kein Produktivitätsdashboard. Nutze sie nicht, um auf die Codequalität oder
die Leistung einzelner Personen zu schließen. Verwende [Workspace-Analysen](/de-DE/codex/enterprise/workspace-analytics)
oder die [Analytics API](/de-DE/codex/enterprise/analytics-api) für Berichte zur Nutzung.

## Erste Schritte

1. Öffne die [Admin-API-Referenz](https://chatgpt.com/public/admin/api-reference) und
   prüfe, ob du mit deiner Administratorrolle auf die benötigten
   Compliance-Ressourcen zugreifen kannst.
2. Nutze für die fortlaufende Erfassung den Compliance-Protokollstream, an den nur neue Einträge angehängt werden können.
Prüfe in der API-Referenz, welche Ressourcen und
Abrufmuster derzeit unterstützt werden.
3. [Lade Protokolldateien herunter](#download-logs) und teste außerhalb der Produktionsumgebung die Datenübernahme
   in ein SIEM-System (Security Information and Event Management) oder einen Data Lake.
4. Plane die kontinuierliche Erfassung ein und wende die Zugriffs-,
Aufbewahrungs- und Legal-Hold-Kontrollen deiner Organisation auf exportierte Datensätze an. Gehe nicht davon aus, dass der
Aufbewahrungszeitraum der Quelle die Aufbewahrungsrichtlinie deiner Organisation ersetzt.

Ein Sicherheitsteam kann beispielsweise unveränderliche Compliance-Ereignisse für Untersuchungen in sein
SIEM streamen oder diese Ereignisse in einen genehmigten E-Discovery-Arbeitsablauf
weiterleiten. Entnimm die aktuellen Routen und Schemas der API-Referenz,
statt eine Endpunktspezifikation aus diesem Leitfaden zu kopieren.

### Protokolle herunterladen

Lade das [Bash-Skript](/downloads/compliance-api/download_compliance_files.sh)
oder das [PowerShell-Skript](/downloads/compliance-api/download_compliance_files.ps1) herunter.
Beide listen alle verfügbaren Protokolldateien nach einem angegebenen Zeitstempel auf und laden sie herunter. Sie durchlaufen dabei alle Ergebnisseiten
und schreiben JSONL in die Standardausgabe. Fehler werden in die Standardfehlerausgabe geschrieben.

Setze `COMPLIANCE_API_KEY` auf deinen Schlüssel für die Enterprise Compliance API. Ersetze
`<workspace_or_org_id>` durch die ID deines ChatGPT-Workspaces oder die ID deiner Organisation auf der API-Plattform
und `<after>` durch einen ISO-8601-Zeitstempel mit Zeitzonenangabe.
Dieses Beispiel ruft jeweils 100 `AUTH_LOG`-Dateien ab.

Installiere unter macOS oder Linux Bash, `curl` und `jq` und führe dann Folgendes aus:

```bash
bash ./download_compliance_files.sh "<workspace_or_org_id>" AUTH_LOG 100 "<after>" > output.jsonl

Das Windows-Skript unterstützt PowerShell 5.1 oder neuer. Überprüfe die heruntergeladene Datei.
Wenn Windows sie blockiert und die Ausführungsrichtlinie deiner Organisation es erlaubt, führe
`Unblock-File -Path .\download_compliance_files.ps1` aus. Dieses Beispiel verwendet
PowerShell 7, um Daten in UTF-8 ohne Byte Order Mark zu speichern:

```powershell
.\download_compliance_files.ps1 "<workspace_or_org_id>" AUTH_LOG 100 "<after>" |
  Set-Content -Encoding utf8NoBOM output.jsonl

## Administrative Abgrenzung prüfen

Der Umfang der Compliance-Daten richtet sich nach dem ChatGPT-Workspace und den Produkten,
die in der aktuellen API-Referenz aufgeführt sind. Für Organisationsdaten der Plattform-API gelten
eigene Kontrollmechanismen für API-Daten und Administration.

Die API-Referenz ist die maßgebliche Quelle für aktuelle Routen, abgedeckte Ereignisse, Schemas,
Filter, das Aufbewahrungsverhalten, erforderliche Berechtigungen und die Abläufe bei Anfragen.
Diese Seite wiederholt die Spezifikation nicht.

## Weiterführende Dokumentation

- [Workspace-Analysen](/de-DE/codex/enterprise/workspace-analytics)
- [Leitfaden für den administrativen Rollout](/de-DE/codex/enterprise/admin-setup)
- [Governance](/de-DE/codex/enterprise/governance)
- [Analytics API](/de-DE/codex/enterprise/analytics-api)

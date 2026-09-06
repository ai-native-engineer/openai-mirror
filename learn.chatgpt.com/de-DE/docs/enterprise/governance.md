<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/governance -->

Governance für Codex-Aktivitäten umfasst interaktive Analysen, programmatische
Berichterstellung, zugehörige Einstellungen zur Steuerung der ChatGPT-Nutzung und Audit-Protokolle. Wähle die
Oberfläche passend zur jeweiligen Frage aus. Analyse- und Compliance-Daten dienen
unterschiedlichen Zwecken.

<a id="governance-and-observability"></a>
<a id="ways-to-track-codex-usage"></a>

| Wenn du Folgendes tun möchtest                                          | Beginne mit                                                                |
| ------------------------------------------------------- | ------------------------------------------------------------------------- |
| Die Nutzung von ChatGPT insgesamt nachvollziehen                      | [Workspace-Analysen](/de-DE/codex/enterprise/workspace-analytics)              |
| Verbreitung und Aktivitäten von Codex interaktiv prüfen        | [Codex-Analysen](#analytics-dashboard)                                   |
| Aggregierte Codex-Berichte in ein anderes System laden     | [Analytics API](/de-DE/codex/enterprise/analytics-api)                          |
| Datensätze für Audits oder Untersuchungen exportieren               | [Compliance API](/de-DE/codex/enterprise/compliance-api)                        |
| Planabhängige Einstellungen für Credits im ChatGPT-Workspace prüfen | [ChatGPT-Nutzungslimits und Ausgabensteuerung](/de-DE/codex/enterprise/usage-limits) |

## Administrationsoberflächen öffnen

- Öffne [Workspace-Analysen](https://chatgpt.com/admin/usage) für interaktive
  Berichte zum Workspace. Der [Leitfaden zu Workspace-Analysen](https://help.openai.com/en/articles/10875114-workspace-analytics-for-chatgpt-enterprise-and-edu)
  beschreibt die aktuellen Rollen und Ansichten.
- Öffne die [Referenz zur Codex Analytics API](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics),
  wenn du geplante, programmatisch erstellte Berichte benötigst.
- Öffne die [Referenz zur Admin API](https://chatgpt.com/public/admin/api-reference)
  und den [Leitfaden zur Compliance-Plattform](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers)
  für Integrationen zur Unterstützung von Audits und Untersuchungen.

Verwende beispielsweise Workspace-Analysen, um die Nutzung schnell zu prüfen, die Analytics API,
um aggregierte Codex-Berichte in ein Business-Intelligence-System zu laden,
und die Compliance API, um auditierbare Datensätze an ein SIEM oder einen Arbeitsablauf für
E-Discovery zu senden.

## Analyse-Dashboard

<a id="dashboard-views"></a>
<a id="data-export"></a>

ChatGPT bietet für den gesamten Workspace Analysen zur Verbreitung und Nutzungsintensität.
Codex-Analysen konzentrieren sich auf Codex-Aktivitäten. Beide sind interaktive
Berichtsoberflächen und keine unverarbeiteten Audit-Protokolle.

Unter [Workspace-Analysen](/de-DE/codex/enterprise/workspace-analytics) kannst du die
beiden Analyseoberflächen vergleichen und findest die aktuellen zugehörigen Quellen, die von den jeweils Verantwortlichen gepflegt werden. Du kannst auch
[Workspace-Analysen](https://chatgpt.com/admin/usage) direkt öffnen. Verwende
Dashboard-Beschriftungen oder Felder in heruntergeladenen Berichten nicht als dauerhaft verlässliche Grundlage für deine Berichterstellung.
Sie können sich mit der Weiterentwicklung des Produkts ändern.

## Zugehörige Einstellungen für die ChatGPT-Nutzung

Die Einstellungen zur Steuerung der ChatGPT-Workspace-Nutzung sind von Analysen getrennt und
legen keine Funktionsberechtigungen fest. Je nach Plan können dafür anrechenbare Codex-Aktivitäten
ChatGPT-Workspace-Credits verbrauchen. Sind Limits ausgeschöpft, kann der Zugriff auf
entsprechende Funktionen vorübergehend ausgesetzt werden. Diese Einstellungen legen weder ein allgemeingültiges Codex-Limit fest noch regeln sie die
Abrechnung für die Platform API.

Unter [ChatGPT-Nutzungslimits und Ausgabensteuerung](/de-DE/codex/enterprise/usage-limits)
findest du die dauerhaft gültige Abgrenzung und die aktuellen Quellen im Hilfecenter.

## Analytics API

<a id="what-it-measures"></a>
<a id="endpoints"></a>
<a id="usage"></a>
<a id="code-review-activity"></a>
<a id="user-engagement-with-code-review"></a>
<a id="how-it-works"></a>
<a id="common-use-cases"></a>

Nutze die Analytics API für die programmatische Erstellung aggregierter Codex-Berichte. Sie
eignet sich für Data-Warehouses, Business-Intelligence-Systeme und die interne
Berichterstellung, die nicht von einem interaktiven Dashboard abhängen soll.

Die API-Referenz enthält die maßgeblichen Angaben zu Zugriffsanforderungen, Routen, Schemas,
Feldern, Berichtszeiträumen und Paginierung. Unter
[Analytics API](/de-DE/codex/enterprise/analytics-api) findest du die konzeptionelle Abgrenzung der Integration
und den Link zur maßgeblichen Referenz.

## Compliance API

<a id="what-it-measures-1"></a>
<a id="what-you-can-export"></a>
<a id="activity-logs"></a>
<a id="metadata-for-audit-and-investigation"></a>
<a id="common-use-cases-1"></a>
<a id="what-it-does-not-provide"></a>

Verwende die Compliance API für Arbeitsabläufe in den Bereichen Sicherheit, Recht und Governance, die
auditierbare Datensätze benötigen. Sie ist kein Dashboard für Nutzung oder Produktivität.

Die API-Referenz enthält die maßgeblichen Angaben zum Umfang der erfassten Ereignisse, zu Schemas und Berechtigungen,
zu Filtern, zur Datenaufbewahrung und zum Verhalten bei Anfragen. Unter
[Compliance API](/de-DE/codex/enterprise/compliance-api) findest du die konzeptionelle Abgrenzung der Integration
und den Link zur maßgeblichen Referenz.

<a id="recommended-pattern"></a>

Nutze für die Rollout-Reihenfolge und die Überprüfung auf diesen Oberflächen den
[Leitfaden für den administrativen Rollout](/de-DE/codex/enterprise/admin-setup).

## Weiterführende Dokumentation

- [Leitfaden für den administrativen Rollout](/de-DE/codex/enterprise/admin-setup)
- [Workspace-Analysen](/de-DE/codex/enterprise/workspace-analytics)
- [Analytics API](/de-DE/codex/enterprise/analytics-api)
- [Compliance API](/de-DE/codex/enterprise/compliance-api)

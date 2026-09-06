<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/workspace-analytics -->

Nutze ChatGPT-Workspace-Analysen, um die Verbreitung im gesamten Workspace auszuwerten. Nutze Codex-Analysen
für Berichte mit Fokus auf Codex. Nutze die Analytics API für programmatisch
abrufbare aggregierte Daten und die Compliance API für prüfbare Datensätze.

Diese Berichtsoptionen gewähren keinen Produktzugriff und legen keine Laufzeitrichtlinien fest. Unter
[Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions)
erfährst du, welche Grenzen bei der Administration gelten.

## Berichtsoption auswählen

| Option                     | Geeignet für                                                    | Maßgebliche Referenz                                                                                                         |
| --------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| ChatGPT-Workspace-Analysen | Interaktive Berichte zur Verbreitung und Nutzung im gesamten Workspace | [Hilfecenter-Leitfaden zu Workspace-Analysen](https://help.openai.com/en/articles/10875114)                               |
| Codex-Analysen             | Interaktive Berichte mit Fokus auf Verbreitung und Nutzung von Codex  | Das nach der Authentifizierung zugängliche [Dashboard für Codex-Analysen](https://admin.openai.com/analytics/codex)                                |
| Analytics API               | Programmatisch abrufbare, aggregierte Berichte zu Codex                      | Die [Referenz zur Codex Analytics API](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics) |
| Compliance API              | Datensätze für Audits, Sicherheit, rechtliche Belange und Untersuchungen             | Die [Referenz zur Admin API](https://chatgpt.com/public/admin/api-reference)                                              |

## ChatGPT-Workspace-Analysen ansehen

ChatGPT-Workspace-Analysen bieten eine interaktive Übersicht über die Verbreitung und
Nutzung der unterstützten Workspace-Funktionen. Verfügbarkeit, Rollen, Dashboard-Bereiche,
Aktualität der Daten, Datenschutzeigenschaften und Exportformate können sich ändern. Unter
[Workspace-Analysen für ChatGPT Enterprise und Edu](https://help.openai.com/en/articles/10875114)
findest du aktuelle Informationen zum Funktionsumfang und zu den Abläufen.

Behandle heruntergeladene Berichte als Organisationsdaten mit Personenbezug.
Wende die Richtlinie deiner Organisation für Zugriff, Speicherung und Aufbewahrung an. Gehe nicht
davon aus, dass ein Export dieselben Datenschutzeigenschaften hat wie ein aggregiertes
Dashboard.

## Codex-Analysen ansehen

Das nach der Authentifizierung zugängliche [Dashboard für Codex-Analysen](https://admin.openai.com/analytics/codex)
konzentriert sich auf Berichte zu Codex. Nutze es für interaktive Analysen, nicht als Garantie für ein
stabiles Schema. Dashboard-Kategorien, Felder, Filter und Exportformate können sich
unabhängig von dieser Seite ändern.

Nutze für automatisierte Berichte die [Analytics API](/de-DE/codex/enterprise/analytics-api)
und richte dich nach der zugehörigen API-Referenz. Nutze für prüfbare Datensätze die
[Compliance API](/de-DE/codex/enterprise/compliance-api).

## Berichtsdaten interpretieren

Beachte dabei folgende Abgrenzungen:

- ChatGPT-Workspace-Analysen und Codex-Analysen decken unterschiedliche
Produktbereiche ab.
- Aggregierte Analysedaten und Audit-Datensätze dienen unterschiedlichen Zwecken und
unterliegen jeweils eigenen Spezifikationen.
- Analysedaten beschreiben Aktivitäten; sie gewähren keinen Zugriff und ändern keine
Laufzeitberechtigungen.
- [ChatGPT-Nutzungslimits und Ausgabenkontrollen](/de-DE/codex/enterprise/usage-limits) stellen
  eine gesonderte, tarifabhängige Beschränkung auf Workspace-Ebene dar.
